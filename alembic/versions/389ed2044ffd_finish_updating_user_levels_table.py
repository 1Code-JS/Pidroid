"""Finish updating user levels table

Revision ID: 389ed2044ffd
Revises: c8d1a40ab779
Create Date: 2023-04-10 20:59:14.387394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '389ed2044ffd'
down_revision = 'c8d1a40ab779'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UserLevels',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('guild_id', sa.BigInteger(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('total_xp', sa.BigInteger(), server_default='0', nullable=True),
    sa.Column('current_xp', sa.BigInteger(), server_default='0', nullable=True),
    sa.Column('xp_to_next_level', sa.BigInteger(), server_default='100', nullable=True),
    sa.Column('level', sa.BigInteger(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('GuildConfigurations', sa.Column('xp_multiplier', sa.Float(), server_default='1.0', nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('GuildConfigurations', 'xp_multiplier')
    op.drop_table('UserLevels')
    # ### end Alembic commands ###