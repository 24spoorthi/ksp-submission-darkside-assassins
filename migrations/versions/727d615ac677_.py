"""empty message

Revision ID: 727d615ac677
Revises: 
Create Date: 2023-02-01 13:13:04.581022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '727d615ac677'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('role', sa.String(length=1), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('designation', sa.String(length=25), nullable=True),
    sa.Column('emVerified', sa.Boolean(), nullable=True),
    sa.Column('phVerified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
