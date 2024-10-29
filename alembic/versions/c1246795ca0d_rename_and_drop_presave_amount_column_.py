"""rename and drop presave_amount column in balance

Revision ID: c1246795ca0d
Revises: 322c7e058515
Create Date: 2024-10-29 19:57:20.538839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1246795ca0d'
down_revision: Union[str, None] = '322c7e058515'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop "presave_amount" column
    op.drop_column('balance', 'presave_amount')

def downgrade():
    # Reverse the drop by adding "presave_amount" back
    op.add_column('balance', sa.Column('presave_amount', sa.Numeric))  # Adjust type if needed
