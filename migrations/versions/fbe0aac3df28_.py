"""empty message

Revision ID: fbe0aac3df28
Revises: 
Create Date: 2021-03-18 00:47:58.817266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbe0aac3df28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('propertytitle', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('noofrooms', sa.String(length=20), nullable=True),
    sa.Column('noofbathrooms', sa.String(length=20), nullable=True),
    sa.Column('price', sa.String(length=200), nullable=True),
    sa.Column('propertytype', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###
