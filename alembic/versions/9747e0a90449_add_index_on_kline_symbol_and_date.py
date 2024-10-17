"""add index on kline symbol and date

Revision ID: 9747e0a90449
Revises: 46edc931127e
Create Date: 2024-10-17 23:01:05.349097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9747e0a90449'
down_revision: Union[str, None] = '46edc931127e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create index on `symbol` column
    op.create_index('idx_kline_symbol', 'kline', ['symbol'])

    # Create composite index on `symbol` and `date` columns
    op.create_index('idx_kline_symbol_date', 'kline', ['symbol', 'date'])


def downgrade():
    # Drop composite index on `symbol` and `date`
    op.drop_index('idx_kline_symbol_date', table_name='kline')

    # Drop index on `symbol`
    op.drop_index('idx_kline_symbol', table_name='kline')