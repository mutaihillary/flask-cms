"""added add_sidebar and short_url to pages

Revision ID: 4b05117ecfd0
Revises: 3b4303875c75
Create Date: 2014-07-11 20:10:44.442097

"""

# revision identifiers, used by Alembic.
revision = '4b05117ecfd0'
down_revision = '3b4303875c75'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pages', sa.Column('add_sidebar', sa.Boolean(), nullable=True))
    op.add_column('pages', sa.Column('short_url', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pages', 'short_url')
    op.drop_column('pages', 'add_sidebar')
    ### end Alembic commands ###