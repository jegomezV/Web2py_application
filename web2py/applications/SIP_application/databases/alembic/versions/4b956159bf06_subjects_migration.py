"""Subjects migration

Revision ID: 4b956159bf06
Revises: daf6b251ed47
Create Date: 2024-03-20 14:19:49.371908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text



# revision identifiers, used by Alembic.
revision: str = '4b956159bf06'
down_revision: Union[str, None] = 'daf6b251ed47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'subjects'"))
    if not result.fetchone():
        # Subjects table
        op.create_table(
            'subjects',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
        )

def downgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'subjects'"))
    if result.fetchone():
        op.drop_table('subjects')
