"""rename num_share to share_qty in inventory

Revision ID: 322c7e058515
Revises: a7dc8ae86055
Create Date: 2024-10-29 19:54:54.323455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '322c7e058515'
down_revision: Union[str, None] = 'a7dc8ae86055'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Rename column from "num_share" to "share_qty" in "inventory" table
    op.alter_column('inventory', 'num_share', new_column_name='share_qty')


def downgrade():
    # Reverse the rename if needed
    op.alter_column('inventory', 'share_qty', new_column_name='num_share')
