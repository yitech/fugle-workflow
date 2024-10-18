"""Add primary key to id and unique index to symbol in market_metadata

Revision ID: 202a34c165e2
Revises: 594bb8aa21eb
Create Date: 2024-10-18 08:47:02.297526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '202a34c165e2'
down_revision: Union[str, None] = '594bb8aa21eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    # Step 1: Drop the existing "market_metadata" table if it exists
    op.drop_table('market_metadata')

    # Step 2: Create a new "market_metadata" table with a primary key
    op.create_table(
        'market_metadata',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('symbol', sa.String(255), nullable=False, unique=True),
        sa.Column('category', sa.String(255), nullable=True),
    )


def downgrade():
    # Drop the new "market_metadata" table
    op.drop_table('market_metadata')