"""add unique constraint on symbol and date

Revision ID: 594bb8aa21eb
Revises: 9747e0a90449
Create Date: 2024-10-17 23:13:53.108089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '594bb8aa21eb'
down_revision: Union[str, None] = '9747e0a90449'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create a unique constraint on symbol and date columns
    op.create_unique_constraint('uq_kline_symbol_date', 'kline', ['symbol', 'date'])


def downgrade():
    # Drop the unique constraint if the migration is rolled back
    op.drop_constraint('uq_kline_symbol_date', 'kline', type_='unique')
