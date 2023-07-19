from __future__ import annotations

from discord import Guild, Role, TextChannel
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from pidroid.utils.api import API, GuildConfigurationTable

class GuildPrefixes:

    def __init__(self, prefixes: List[str]) -> None:
        self.__prefixes = prefixes

    @property
    def prefixes(self) -> List[str]:
        """A list of guild prefixes."""
        return self.__prefixes

class GuildConfiguration:

    def __init__(self, api: API) -> None:
        self.api = api

    @classmethod
    def from_table(cls: type[GuildConfiguration], api: API, table: GuildConfigurationTable) -> GuildConfiguration:
        """Constructs level reward from a LevelRewardsTable object."""
        obj = cls(api)
        obj.__from_table(table)
        return obj

    def __from_table(self, table: GuildConfigurationTable) -> None:
        """Creates a GuildConfiguration object from a table object."""
        self.__id: int = table.id # type: ignore
        self.__guild_id: int = table.guild_id # type: ignore

        self.__prefixes: List[str] = table.prefixes # type: ignore

        self.__jail_channel_id: Optional[int] = table.jail_channel # type: ignore
        self.__jail_role_id: Optional[int] = table.jail_role # type: ignore
        self.__log_channel_id: Optional[int] = table.log_channel # type: ignore

        self.__public_tags: bool = table.public_tags # type: ignore
        self.__allow_punishing_moderators: bool = table.punishing_moderators # type: ignore

        self.__suspicious_usernames: List[str] = table.suspicious_usernames # type: ignore

        self.__appeal_url: Optional[str] = table.appeal_url # type: ignore

        # XP system related information
        self.__xp_system_active: bool = table.xp_system_active # type: ignore
        self.__xp_multiplier = table.xp_multiplier
        self.__xp_per_message_min = table.xp_per_message_min
        self.__xp_per_message_max = table.xp_per_message_max
        self.__xp_exempt_roles = table.xp_exempt_roles
        self.__xp_exempt_channels = table.xp_exempt_channels
        self.__stack_level_rewards: bool = table.stack_level_rewards # type: ignore

    @property
    def guild_id(self) -> int:
        """The ID of the guild this configuration belongs to."""
        return self.__guild_id

    @property
    def guild(self) -> Optional[Guild]:
        """The guild this configuration belongs to."""
        return self.api.client.get_guild(self.__guild_id)

    @property
    def guild_prefixes(self) -> GuildPrefixes:
        """Returns GuildPrefixes object."""
        return GuildPrefixes(self.__prefixes)
    
    @property
    def jail_channel_id(self) -> Optional[int]:
        """Returns the ID of the jail channel, if available."""
        return self.__jail_channel_id
    
    @jail_channel_id.setter
    def jail_channel_id(self, id: int) -> None:
        self.__jail_channel_id = id

    @property
    def jail_role_id(self) -> Optional[int]:
        """Returns the ID of the jail role, if available."""
        return self.__jail_role_id

    @jail_role_id.setter
    def jail_role_id(self, id: int) -> None:
        self.__jail_role_id = id

    @property
    def logging_channel_id(self) -> Optional[int]:
        """Returns the ID of the logging channel if available."""
        return self.__log_channel_id

    @property
    def public_tags(self) -> bool:
        """Returns true if tag system can be management by regular members."""
        return self.__public_tags
    
    async def toggle_public_tags(self) -> None:
        """Updates public tags permission."""
        self.__public_tags = not self.__public_tags
        await self._update()

    @property
    def allow_to_punish_moderators(self) -> bool:
        """Returns true if moderators are allowed to punish lower ranking moderators."""
        return self.__allow_punishing_moderators
    
    async def toggle_moderator_punishing(self) -> None:
        """Updates moderator punishing permission."""
        self.__allow_punishing_moderators = not self.__allow_punishing_moderators
        await self._update()

    async def _update(self) -> None:
        await self.api._update_guild_configuration(
            self.__id,
            jail_channel=self.__jail_channel_id,
            jail_role=self.__jail_role_id,
            log_channel=self.__log_channel_id,
            prefixes=self.__prefixes,
            suspicious_usernames=self.__suspicious_usernames,
            public_tags=self.__public_tags,
            punishing_moderators=self.__allow_punishing_moderators,
            appeal_url=self.__appeal_url,
            xp_system_active=self.__xp_system_active,
            stack_level_rewards=self.__stack_level_rewards
        )

    async def delete(self) -> None:
        """Deletes the current guild configuration from the database."""
        await self.api.delete_guild_configuration(self.__id)

    """XP system related"""

    @property
    def xp_system_active(self) -> bool:
        """Returns true if the XP system is active for the server."""
        return self.__xp_system_active # type: ignore
    
    async def toggle_xp_system(self) -> None:
        """Toggles XP system."""
        self.__xp_system_active = not self.__xp_system_active
        await self._update()

    @property
    def xp_multiplier(self) -> float:
        """Returns the XP multiplier per message."""
        return self.__xp_multiplier # type: ignore
    
    @property
    def xp_per_message_min(self) -> int:
        """Returns the minimum amount of XP that can be received per message."""
        return self.__xp_per_message_min # type: ignore

    @property
    def xp_per_message_max(self) -> int:
        """Returns the maximum amount of XP that can be received per message."""
        return self.__xp_per_message_max # type: ignore

    @property
    def xp_exempt_roles(self) -> List[int]:
        """Returns a list of XP exempt role IDs."""
        return self.__xp_exempt_roles # type: ignore

    @property
    def xp_exempt_channels(self) -> List[int]:
        """Returns a list of XP exempt channel IDs."""
        return self.__xp_exempt_channels # type: ignore

    @property
    def level_rewards_stacked(self) -> bool:
        """Returns true if level rewards obtained from the level system should be stacked."""
        return self.__stack_level_rewards # type: ignore
    
    async def toggle_level_reward_stacking(self) -> None:
        """Toggles level reward stacking."""
        self.__stack_level_rewards = not self.__stack_level_rewards
        await self._update()

    """Logging system related"""
    
    @property
    def logging_active(self) -> bool:
        """Returns true if logging system is enabled for the server."""
        return True # TODO: fix


    """Suggestions related"""

    @property
    def suggestion_system_active(self) -> bool:
        """Returns true if suggestion system is enabled for the server."""
        raise NotImplementedError
    
    async def toggle_suggestion_system(self) -> None:
        """Toggles suggestion system."""
        raise NotImplementedError

    @property
    def suggestions_channel_id(self) -> Optional[int]:
        """Returns the ID of the suggestions channel if available."""
        raise NotImplementedError

    @property
    def suggestion_threads_enabled(self) -> bool:
        """Returns true if expiring thread creation is enabled for the suggestion system."""
        raise NotImplementedError

    async def toggle_suggestion_threads(self) -> None:
        """Toggles threads for the suggestion system."""
        raise NotImplementedError

    """Punishment system related"""

    @property
    def appeal_url(self) -> Optional[str]:
        """Returns the punishment appeal URL."""
        return self.__appeal_url

    async def update_public_tag_permission(self, allow_public: bool) -> None:
        """Updates public tag permission."""
        self.__public_tags = allow_public
        await self._update()

    async def update_prefixes(self, prefix: str) -> None:
        """Updates the guild bot prefixes."""
        self.__prefixes = [prefix]
        await self._update()

    async def update_jail_channel(self, channel: Optional[TextChannel]) -> None:
        """Updates the guild jail text channel."""
        if channel is None:
            self.__jail_channel_id = None
        else:
            self.__jail_channel_id = channel.id
        await self._update()

    async def update_jail_role(self, role: Optional[Role]) -> None:
        """Updates the guild jail role."""
        if role is None:
            self.__jail_role_id = None
        else:
            self.__jail_role_id = role.id
        await self._update()

    async def update_log_channel(self, channel: Optional[TextChannel]) -> None:
        """Updates the guild log text channel."""
        if channel is None:
            self.__log_channel_id = None
        else:
            self.__log_channel_id = channel.id
        await self._update()

    async def update_appeal_url(self, appeal_url: Optional[str]) -> None:
        """Updates the appeal URL. If None is specified, the appeal URL is removed."""
        self.__appeal_url = appeal_url
        await self._update()

    async def fetch_all_level_rewards(self):
        """Returns a list of all level rewards in the guild."""
        return await self.api.fetch_all_guild_level_rewards(self.__guild_id)
    
    async def fetch_member_level(self, member_id: int):
        """Returns member level object."""
        return await self.api.fetch_user_level_info(self.__guild_id, member_id)

    async def fetch_all_member_levels(self):
        """Returns a list of member level information for every member in the guild."""
        return await self.api.fetch_guild_level_infos(self.__guild_id)
