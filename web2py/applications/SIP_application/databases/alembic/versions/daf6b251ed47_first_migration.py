"""First migration

Revision ID: daf6b251ed47
Revises: 
Create Date: 2024-03-20 14:03:01.306943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = 'daf6b251ed47'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'students'"))
    if not result.fetchone():
        # Students table
        op.create_table(
            'students',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False, unique=True),
        )

def downgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'students'"))
    if result.fetchone():
        op.drop_table('students')
