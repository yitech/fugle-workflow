"""create inventory table

Revision ID: 46edc931127e
Revises: d7734bd10509
Create Date: 2024-10-17 10:34:36.567165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46edc931127e'
down_revision: Union[str, None] = 'd7734bd10509'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the 'inventory' table
    op.create_table(
        'inventory',
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('symbol', sa.String(), nullable=False),
        sa.Column('num_share', sa.Integer(), nullable=False),
    )

def downgrade():
    # Drop the 'inventory' table
    op.drop_table('inventory')