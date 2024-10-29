"""drop settlement table

Revision ID: 3fb1b894f94e
Revises: c1246795ca0d
Create Date: 2024-10-29 19:58:38.676990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fb1b894f94e'
down_revision: Union[str, None] = 'c1246795ca0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop the "settlement" table
    op.drop_table('settlement')

def downgrade():
    # Recreate the "settlement" table if needed (adjust columns and types)
    op.create_table(
        'settlement',
        sa.Column('id', sa.Integer, primary_key=True),
        # Add other columns that were in the "settlement" table
    )
