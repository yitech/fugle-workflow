"""create market_metadata table

Revision ID: d9cfc9ecdbce
Revises: 
Create Date: 2024-10-15 22:14:15.116643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9cfc9ecdbce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'market_metadata',
        sa.Column('symbol', sa.String(), nullable=False),
        sa.Column('type', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('market_metadata')
