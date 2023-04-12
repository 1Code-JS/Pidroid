from __future__ import annotations

from discord import Guild, Member, User, app_commands, Role
from discord.utils import escape_markdown
from discord.ext import commands # type: ignore
from discord.ext.commands import Context
from discord.ext.commands.errors import BadArgument # type: ignore
from typing import List, Optional, Union
from typing_extensions import Annotated

from pidroid.client import Pidroid
from pidroid.models.categories import LevelCategory
from pidroid.utils.embeds import PidroidEmbed, SuccessEmbed
from pidroid.utils.levels import LevelInformation
from pidroid.utils.paginators import ListPageSource, PidroidPages

class LeaderboardPaginator(ListPageSource):
    def __init__(self, data: List[LevelInformation]):
        super().__init__(data, per_page=10)
        self.embed = PidroidEmbed(title='Leaderboard rankings')

    async def format_page(self, menu: PidroidPages, data: List[LevelInformation]):
        assert isinstance(menu.ctx.bot, Pidroid)
        self.embed.clear_fields()
        for info in data:
            self.embed.add_field(
                name=f"{info.rank}. {await menu.ctx.bot.get_or_fetch_user(info.user_id)} (lvl. {info.current_level})",
                value=f'{info.total_xp} XP',
                inline=False
            )
        return self.embed

class LevelCommands(commands.Cog): # type: ignore
    """This class implements a cog for special bot owner only commands."""
    def __init__(self, client: Pidroid) -> None:
        self.client = client

    async def check_system_enabled(self, guild: Guild) -> bool:
        """Checks if the XP system is enabled in the specified guild.
        
        Raises BadArgument if system is not enabled."""
        conf = await self.client.fetch_guild_configuration(guild.id)
        if not conf.xp_system_active:
            raise BadArgument('XP system is not enabled in this server!')
        return True

    @commands.hybrid_command( # type: ignore
        name="rank",
        brief="Displays the member level rank.",
        usage="[user/member]",
        category=LevelCategory
    )
    @app_commands.describe(member="Member or user you to view rank of.")
    @commands.guild_only()
    @commands.bot_has_guild_permissions(send_messages=True)
    async def rank_command(
        self,
        ctx: Context,
        member: Annotated[Optional[Union[Member, User]], Union[Member, User]] = None
    ):
        assert ctx.guild is not None
        await self.check_system_enabled(ctx.guild)
        member = member or ctx.author
        info = await self.client.api.fetch_member_level_info(ctx.guild.id, member.id)
        if info is None:
            raise BadArgument('The specified member is not yet ranked!')

        embed = PidroidEmbed(title=f'{escape_markdown(str(member))} rank')
        avatar = member.avatar or member.default_avatar
        embed.set_thumbnail(url=avatar.url)
        embed.add_field(name='Level', value=info.current_level)
        embed.add_field(name='Rank', value=f'#{info.rank}')       

        # Create a progress bar
        # https://github.com/KumosLab/Discord-Levels-Bot/blob/b01e22a9213b004eed5f88d68b500f4f4cd04891/KumosLab/Database/Create/RankCard/text.py
        dashes = 10
        current_dashes = int(info.current_xp / int(info.xp_to_level_up / dashes))
        current_prog = '🟦' * current_dashes
        remaining_prog = '⬛' * (dashes - current_dashes)

        embed.add_field(name=f'Level progress ({info.current_xp} / {info.xp_to_level_up} XP)', value=f"{current_prog}{remaining_prog}", inline=False)

        await ctx.reply(embed=embed)
        
    @commands.hybrid_command( # type: ignore
        name='leaderboard',
        brief='Returns the server level leaderboard.',
        category=LevelCategory
    )
    @commands.guild_only()
    @commands.bot_has_guild_permissions(send_messages=True) # type: ignore
    async def leaderboard_command(self, ctx: Context):
        assert ctx.guild is not None
        await self.check_system_enabled(ctx.guild)
        levels = await self.client.api.fetch_guild_levels(ctx.guild.id, limit=100)
        pages = PidroidPages(LeaderboardPaginator(levels), ctx=ctx)
        return await pages.start()

    @commands.hybrid_group( # type: ignore
        name='rewards',
        brief='Returns the server level rewards.',
        category=LevelCategory,
        invoke_without_command=True,
        fallback='list'
    )
    @commands.bot_has_permissions(send_messages=True) # type: ignore
    @commands.guild_only() # type: ignore
    async def rewards_command(self, ctx: Context):
        if ctx.invoked_subcommand is None:
            assert ctx.guild is not None
            await self.check_system_enabled(ctx.guild)
            rewards = await self.client.api.fetch_all_guild_level_rewards(ctx.guild.id)
            if len(rewards) == 0:
                raise BadArgument('This server does not have any level rewards!')
            
            embed = PidroidEmbed(title='Server level rewards')
            embed.description = ""
            # TODO: ensure there is no overflow
            for reward in rewards:
                role = await self.client.get_or_fetch_role(ctx.guild, reward.role_id)
                role_name = role.mention if role else reward.role_id
                embed.description += f"{reward.level}: {role_name}\n"
            await ctx.reply(embed=embed)

    @rewards_command.command( # type: ignore
        name='add',
        brief='Adds the specified role as a level reward.',
        usage='<role> <level>',
        category=LevelCategory
    )
    @commands.bot_has_permissions(send_messages=True) # type: ignore
    @commands.has_permissions(manage_roles=True) # type: ignore
    @commands.guild_only() # type: ignore
    async def rewards_add_command(self, ctx: Context, role: Role, level: int):
        assert ctx.guild is not None
        await self.check_system_enabled(ctx.guild)
        if level > 1000:
            raise BadArgument('You cannot set level requirement higher than 1000!')
        if level <= 0:
            raise BadArgument('You cannot set level requirement to be 0 or less.')

        reward = await self.client.api.fetch_guild_level_reward_by_level(ctx.guild.id, level)
        if reward is not None:
            raise BadArgument('A role reward already exists for the specified level.')

        reward = await self.client.api.fetch_guild_level_reward_by_role(ctx.guild.id, role.id)
        if reward is not None:
            raise BadArgument('Specified role already belongs to a reward.')

        await self.client.api.insert_level_reward(ctx.guild.id, role.id, level)
        await ctx.reply(embed=SuccessEmbed('Role reward added successfully!'))

    @rewards_command.command( # type: ignore
        name='change',
        brief='Changes the specified role level requirement.',
        usage='<role> <level>',
        category=LevelCategory
    )
    @commands.bot_has_permissions(send_messages=True) # type: ignore
    @commands.has_permissions(manage_roles=True) # type: ignore
    @commands.guild_only() # type: ignore
    async def rewards_change_command(self, ctx: Context, role: Role, level: int):
        assert ctx.guild is not None
        await self.check_system_enabled(ctx.guild)
        if level > 1000:
            raise BadArgument('You cannot set level requirement higher than 1000!')
        if level <= 0:
            raise BadArgument('You cannot set level requirement to be 0 or less.')

        reward = await self.client.api.fetch_guild_level_reward_by_level(ctx.guild.id, level)
        if reward is not None:
            raise BadArgument('A role reward already exists for the specified level.')

        reward = await self.client.api.fetch_guild_level_reward_by_role(ctx.guild.id, role.id)
        if reward is None:
            raise BadArgument('Specified role does not belong to any rewards.')

        await self.client.api.update_level_reward_by_id(reward.internal_id, role.id, level)
        await ctx.reply(embed=SuccessEmbed(f'Role level requirement successfully updated to {level}!'))

    @rewards_command.command( # type: ignore
        name='remove',
        brief='Removes the specified role as a level reward.',
        usage='<role>',
        category=LevelCategory
    )
    @commands.bot_has_permissions(send_messages=True) # type: ignore
    @commands.has_permissions(manage_roles=True) # type: ignore
    @commands.guild_only() # type: ignore
    async def rewards_remove_command(self, ctx: Context, role: Role):
        assert ctx.guild is not None
        await self.check_system_enabled(ctx.guild)
        reward = await self.client.api.fetch_guild_level_reward_by_role(ctx.guild.id, role.id)
        if reward is None:
            raise BadArgument('Specified role does not belong to any rewards.')

        await self.client.api.delete_level_reward(reward.internal_id)
        await ctx.reply(embed=SuccessEmbed('Role reward removed successfully!'))

    # TODO: add exempt role
    # add exempt channel
    # remove exempt role
    # remove exempt channel

async def setup(client: Pidroid) -> None:
    await client.add_cog(LevelCommands(client))
