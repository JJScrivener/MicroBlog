"""add language to posts

Revision ID: 810133d16a9a
Revises: eb5c93f1d967
Create Date: 2022-07-26 18:55:30.651754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '810133d16a9a'
down_revision = 'eb5c93f1d967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
