"""Create kline table

Revision ID: ef1456d0f1c1
Revises: ac797cf2986a
Create Date: 2024-08-25 13:05:51.311304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef1456d0f1c1'
down_revision: Union[str, None] = 'ac797cf2986a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('kline',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('symbol', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('open', sa.Float(), nullable=False),
    sa.Column('high', sa.Float(), nullable=False),
    sa.Column('low', sa.Float(), nullable=False),
    sa.Column('close', sa.Float(), nullable=False),
    sa.Column('volume', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    op.drop_table('kline')
