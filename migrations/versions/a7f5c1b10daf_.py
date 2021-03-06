"""empty message

Revision ID: a7f5c1b10daf
Revises: 
Create Date: 2017-09-05 00:38:03.042967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7f5c1b10daf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('access_token', sa.String(length=255), nullable=False),
    sa.Column('scope', sa.String(length=255), nullable=False),
    sa.Column('team_name', sa.String(length=255), nullable=False),
    sa.Column('team_id', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token')
    )
    op.create_table('period',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.String(length=255), nullable=False),
    sa.Column('user_name', sa.String(length=255), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=False),
    sa.Column('reason', sa.String(length=255), nullable=True),
    sa.Column('access_token_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['access_token_id'], ['access_token.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'start', name='_user_id_start_uq')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('period')
    op.drop_table('access_token')
    # ### end Alembic commands ###
