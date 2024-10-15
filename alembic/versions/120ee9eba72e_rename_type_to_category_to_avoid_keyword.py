"""rename type to category to avoid keyword

Revision ID: 120ee9eba72e
Revises: d9cfc9ecdbce
Create Date: 2024-10-15 22:30:33.865060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '120ee9eba72e'
down_revision: Union[str, None] = 'd9cfc9ecdbce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Renaming column "type" to "category"
    op.alter_column('market_metadata', 'type', new_column_name='category')


def downgrade():
    # Reverting column rename (category back to type)
    op.alter_column('market_metadata', 'category', new_column_name='type')