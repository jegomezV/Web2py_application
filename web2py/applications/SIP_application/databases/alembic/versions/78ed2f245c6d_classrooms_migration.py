"""Classrooms migration

Revision ID: 78ed2f245c6d
Revises: 4b956159bf06
Create Date: 2024-03-20 14:20:45.759321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '78ed2f245c6d'
down_revision: Union[str, None] = '4b956159bf06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'classrooms'"))
    if not result.fetchone():
        # Classrooms table
        op.create_table(
            'classrooms',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
        )

def downgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'classrooms'"))
    if result.fetchone():
        op.drop_table('classrooms')
