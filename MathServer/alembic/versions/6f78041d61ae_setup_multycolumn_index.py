"""setup multycolumn index

Revision ID: 6f78041d61ae
Revises: 638efc8bd773
Create Date: 2022-03-22 05:33:44.837515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f78041d61ae'
down_revision = '638efc8bd773'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('operation', 'expression_data', ['operator', 'num1', 'num2'])


def downgrade():
    op.drop_index('operation', 'expression_data')
