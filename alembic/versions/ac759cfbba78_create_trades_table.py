"""create trades table

Revision ID: ac759cfbba78
Revises: 3fb1b894f94e
Create Date: 2024-10-29 20:40:56.672501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac759cfbba78'
down_revision: Union[str, None] = '3fb1b894f94e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'trade',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('side', sa.String(length=1), nullable=False),
        sa.Column('dt', sa.DateTime, nullable=False),
        sa.Column('fee', sa.Integer, nullable=False),
        sa.Column('order_no', sa.String(length=20), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('qty', sa.Integer, nullable=False),
        sa.Column('symbol', sa.String(length=10), nullable=False),
        sa.Column('tax', sa.Integer, nullable=False),
        sa.Column('trade', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('trade')