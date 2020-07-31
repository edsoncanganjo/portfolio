"""empty message

Revision ID: 6b31fa963abb
Revises: 
Create Date: 2020-07-31 14:21:54.410909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b31fa963abb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('qtd', sa.Integer(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=6), nullable=False),
    sa.Column('last_update', sa.DateTime(timezone=6), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=6), nullable=False),
    sa.Column('last_update', sa.DateTime(timezone=6), nullable=True),
    sa.Column('recovery_code', sa.String(length=200), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('product')
    # ### end Alembic commands ###
