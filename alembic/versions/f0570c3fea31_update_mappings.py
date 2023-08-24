"""Update mappings

Revision ID: f0570c3fea31
Revises: 8c8a4f8ad03f
Create Date: 2023-08-22 18:16:08.264283

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f0570c3fea31'
down_revision = '8c8a4f8ad03f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ExpiringThreads', 'thread_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('ExpiringThreads', 'expiration_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('GuildConfigurations', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('GuildConfigurations', 'prefixes',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               nullable=False,
               existing_server_default=sa.text("'{}'::text[]"))
    op.alter_column('GuildConfigurations', 'public_tags',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'punishing_moderators',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'xp_system_active',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'xp_per_message_min',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'15'::bigint"))
    op.alter_column('GuildConfigurations', 'xp_per_message_max',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'25'::bigint"))
    op.alter_column('GuildConfigurations', 'xp_multiplier',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False,
               existing_server_default=sa.text("'1'::double precision"))
    op.alter_column('GuildConfigurations', 'xp_exempt_roles',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=False,
               existing_server_default=sa.text("'{}'::bigint[]"))
    op.alter_column('GuildConfigurations', 'xp_exempt_channels',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=False,
               existing_server_default=sa.text("'{}'::bigint[]"))
    op.alter_column('GuildConfigurations', 'stack_level_rewards',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('GuildConfigurations', 'suggestion_system_active',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'suggestion_threads_enabled',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.drop_column('GuildConfigurations', 'suspicious_usernames')
    op.alter_column('LevelRewards', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('LevelRewards', 'level',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('LevelRewards', 'role_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('LinkedAccounts', 'user_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('LinkedAccounts', 'forum_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('LinkedAccounts', 'roles',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=False,
               existing_server_default=sa.text("'{}'::bigint[]"))
    op.alter_column('PunishmentCounters', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('PunishmentCounters', 'counter',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'1'::bigint"))
    op.alter_column('Punishments', 'case_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Punishments', 'type',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Punishments', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Punishments', 'user_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Punishments', 'moderator_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Punishments', 'issue_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('Punishments', 'handled',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('Punishments', 'visible',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.alter_column('RoleChangeQueue', 'action',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('RoleChangeQueue', 'status',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('RoleChangeQueue', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('RoleChangeQueue', 'member_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('RoleChangeQueue', 'role_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('RoleChangeQueue', 'date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('Suggestions', 'author_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Suggestions', 'message_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Suggestions', 'suggestion',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Suggestions', 'date_submitted',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('Suggestions', 'attachments',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               nullable=False,
               existing_server_default=sa.text("'{}'::text[]"))
    op.alter_column('Tags', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Tags', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Tags', 'content',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Tags', 'authors',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=False)
    op.alter_column('Tags', 'aliases',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               nullable=False,
               existing_server_default=sa.text("'{}'::text[]"))
    op.alter_column('Tags', 'locked',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('Tags', 'date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('Translations', 'original_content',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Translations', 'detected_language',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Translations', 'translated_string',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('UserLevels', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('UserLevels', 'user_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('UserLevels', 'total_xp',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'0'::bigint"))
    op.alter_column('UserLevels', 'current_xp',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'0'::bigint"))
    op.alter_column('UserLevels', 'xp_to_next_level',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'100'::bigint"))
    op.alter_column('UserLevels', 'level',
               existing_type=sa.BIGINT(),
               nullable=False,
               existing_server_default=sa.text("'0'::bigint"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('UserLevels', 'level',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'0'::bigint"))
    op.alter_column('UserLevels', 'xp_to_next_level',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'100'::bigint"))
    op.alter_column('UserLevels', 'current_xp',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'0'::bigint"))
    op.alter_column('UserLevels', 'total_xp',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'0'::bigint"))
    op.alter_column('UserLevels', 'user_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('UserLevels', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Translations', 'translated_string',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Translations', 'detected_language',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Translations', 'original_content',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Tags', 'date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('Tags', 'locked',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('Tags', 'aliases',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               nullable=True,
               existing_server_default=sa.text("'{}'::text[]"))
    op.alter_column('Tags', 'authors',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=True)
    op.alter_column('Tags', 'content',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Tags', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Tags', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Suggestions', 'attachments',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               nullable=True,
               existing_server_default=sa.text("'{}'::text[]"))
    op.alter_column('Suggestions', 'date_submitted',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('Suggestions', 'suggestion',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Suggestions', 'message_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Suggestions', 'author_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('RoleChangeQueue', 'date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('RoleChangeQueue', 'role_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('RoleChangeQueue', 'member_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('RoleChangeQueue', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('RoleChangeQueue', 'status',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('RoleChangeQueue', 'action',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Punishments', 'visible',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('Punishments', 'handled',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('Punishments', 'issue_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('Punishments', 'moderator_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Punishments', 'user_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Punishments', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Punishments', 'type',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Punishments', 'case_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('PunishmentCounters', 'counter',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'1'::bigint"))
    op.alter_column('PunishmentCounters', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('LinkedAccounts', 'roles',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=True,
               existing_server_default=sa.text("'{}'::bigint[]"))
    op.alter_column('LinkedAccounts', 'forum_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('LinkedAccounts', 'user_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('LevelRewards', 'role_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('LevelRewards', 'level',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('LevelRewards', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.add_column('GuildConfigurations', sa.Column('suspicious_usernames', postgresql.ARRAY(sa.TEXT()), server_default=sa.text("'{}'::text[]"), autoincrement=False, nullable=True))
    op.alter_column('GuildConfigurations', 'suggestion_threads_enabled',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'suggestion_system_active',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'stack_level_rewards',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    op.alter_column('GuildConfigurations', 'xp_exempt_channels',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=True,
               existing_server_default=sa.text("'{}'::bigint[]"))
    op.alter_column('GuildConfigurations', 'xp_exempt_roles',
               existing_type=postgresql.ARRAY(sa.BIGINT()),
               nullable=True,
               existing_server_default=sa.text("'{}'::bigint[]"))
    op.alter_column('GuildConfigurations', 'xp_multiplier',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True,
               existing_server_default=sa.text("'1'::double precision"))
    op.alter_column('GuildConfigurations', 'xp_per_message_max',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'25'::bigint"))
    op.alter_column('GuildConfigurations', 'xp_per_message_min',
               existing_type=sa.BIGINT(),
               nullable=True,
               existing_server_default=sa.text("'15'::bigint"))
    op.alter_column('GuildConfigurations', 'xp_system_active',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'punishing_moderators',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'public_tags',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('GuildConfigurations', 'prefixes',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               nullable=True,
               existing_server_default=sa.text("'{}'::text[]"))
    op.alter_column('GuildConfigurations', 'guild_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('ExpiringThreads', 'expiration_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('ExpiringThreads', 'thread_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    # ### end Alembic commands ###