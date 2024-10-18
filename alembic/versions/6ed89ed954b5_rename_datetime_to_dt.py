"""rename datetime to dt

Revision ID: 6ed89ed954b5
Revises: 202a34c165e2
Create Date: 2024-10-18 22:21:53.134422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ed89ed954b5'
down_revision: Union[str, None] = '202a34c165e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rename 'datetime' to 'dt' for the 'kline' table
    op.alter_column('kline', 'date', new_column_name='dt')

    # Rename 'datetime' to 'dt' for the 'balance' table
    op.alter_column('balance', 'date', new_column_name='dt')

    # Rename 'datetime' to 'dt' for the 'inventory' table
    op.alter_column('inventory', 'date', new_column_name='dt')

    # Rename 'datetime' to 'dt' for the 'settlement' table
    op.alter_column('settlement', 'date', new_column_name='dt')


def downgrade():
    # Reverse the column renaming in case of downgrade
    op.alter_column('kline', 'dt', new_column_name='datetime')
    op.alter_column('balance', 'dt', new_column_name='datetime')
    op.alter_column('inventory', 'dt', new_column_name='datetime')
    op.alter_column('settlement', 'dt', new_column_name='datetime')