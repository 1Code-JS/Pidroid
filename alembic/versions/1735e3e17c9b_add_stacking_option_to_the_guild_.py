"""Add stacking option to the guild configuration

Revision ID: 1735e3e17c9b
Revises: 389ed2044ffd
Create Date: 2023-04-10 22:12:46.871484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1735e3e17c9b'
down_revision = '389ed2044ffd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('GuildConfigurations', sa.Column('stack_level_rewards', sa.Boolean(), server_default='true', nullable=True))
    op.drop_column('LevelRewards', 'level')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('LevelRewards', sa.Column('level', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('GuildConfigurations', 'stack_level_rewards')
    # ### end Alembic commands ###