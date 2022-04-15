"""create data table

Revision ID: 5ddafe44c356
Revises: 
Create Date: 2022-04-15 16:25:22.154431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ddafe44c356'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sequences',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('unsorted', sa.String(16)),
        sa.Column('sorted', sa.String(128))
    )


def downgrade():
    op.drop_table('sequences')
