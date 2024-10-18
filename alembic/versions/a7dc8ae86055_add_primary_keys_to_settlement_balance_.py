"""add primary keys to settlement, balance, and inventory

Revision ID: a7dc8ae86055
Revises: 6ed89ed954b5
Create Date: 2024-10-18 22:26:01.799255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7dc8ae86055'
down_revision: Union[str, None] = '6ed89ed954b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add 'id' column to 'settlement' table
    op.add_column('settlement', sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True))

    # Add 'id' column to 'balance' table
    op.add_column('balance', sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True))

    # Add 'id' column to 'inventory' table
    op.add_column('inventory', sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True))

    # Now create primary key for the 'id' column on each table
    op.create_primary_key('pk_settlement', 'settlement', ['id'])
    op.create_primary_key('pk_balance', 'balance', ['id'])
    op.create_primary_key('pk_inventory', 'inventory', ['id'])


def downgrade():
    # Drop the primary keys and columns in case of downgrade
    op.drop_constraint('pk_settlement', 'settlement', type_='primary')
    op.drop_constraint('pk_balance', 'balance', type_='primary')
    op.drop_constraint('pk_inventory', 'inventory', type_='primary')

    op.drop_column('settlement', 'id')
    op.drop_column('balance', 'id')
    op.drop_column('inventory', 'id')