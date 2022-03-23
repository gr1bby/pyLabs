"""setup indexes

Revision ID: 638efc8bd773
Revises: 
Create Date: 2022-03-22 05:03:17.836961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638efc8bd773'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('expression_data',
    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
    sa.Column('operator', sa.String(10)),
    sa.Column('num1', sa.Numeric()),
    sa.Column('num2', sa.Numeric()),
    sa.Column('result', sa.Numeric())
    )
    op.create_index('op_indx', 'expression_data', ['operator'])
    op.create_index('res_indx', 'expression_data', ['result'])


def downgrade():
    op.drop_table('expression_data')
    op.drop_index('op_indx', 'expression_data')
    op.drop_index('res_indx', 'expression_data')
