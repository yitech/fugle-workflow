"""create balance table

Revision ID: d7734bd10509
Revises: 510fefd7eed4
Create Date: 2024-10-17 10:29:20.763473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7734bd10509'
down_revision: Union[str, None] = '510fefd7eed4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the 'settlement' table
    op.create_table(
        'balance',
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('available', sa.BigInteger(), nullable=True),
        sa.Column('presave_amount', sa.BigInteger(), nullable=True),
    )

def downgrade():
    # Drop the 'settlement' table
    op.drop_table('balance')