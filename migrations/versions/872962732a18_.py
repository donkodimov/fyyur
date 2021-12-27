"""empty message

Revision ID: 872962732a18
Revises: fe592abffea5
Create Date: 2021-12-11 19:30:31.805242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872962732a18'
down_revision = 'fe592abffea5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.drop_constraint('Show_vanue_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.drop_column('Show', 'vanue_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('vanue_id', sa.INTEGER(), autoincrement=False, nullable=False))
    #op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_vanue_id_fkey', 'Show', 'Venue', ['vanue_id'], ['id'])
    op.drop_column('Show', 'venue_id')
    # ### end Alembic commands ###