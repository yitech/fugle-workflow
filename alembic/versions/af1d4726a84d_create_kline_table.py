"""create kline table

Revision ID: af1d4726a84d
Revises: 120ee9eba72e
Create Date: 2024-10-16 20:34:22.987773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af1d4726a84d'
down_revision: Union[str, None] = '120ee9eba72e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'kline',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('symbol', sa.String(255), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('high', sa.Float, nullable=False),
        sa.Column('low', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('volume', sa.BigInteger, nullable=False)
    )

def downgrade():
    op.drop_table('kline')