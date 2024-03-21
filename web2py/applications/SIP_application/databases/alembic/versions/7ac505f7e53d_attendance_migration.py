"""Attendance migration

Revision ID: 7ac505f7e53d
Revises: 78ed2f245c6d
Create Date: 2024-03-20 14:21:30.937660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text



# revision identifiers, used by Alembic.
revision: str = '7ac505f7e53d'
down_revision: Union[str, None] = '78ed2f245c6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'attendance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('student_id', sa.Integer),
        sa.Column('classroom_id', sa.Integer),
        sa.Column('subject_id', sa.Integer),
        sa.Column('attendance_date', sa.DateTime),
        sa.Column('status', sa.String),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='fk_student_id'),
        sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.id'], name='fk_classroom_id'),
        sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name='fk_subject_id'),
    )


def downgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(text("SELECT * FROM information_schema.tables WHERE table_name = 'attendance'"))
    if result.fetchone():
        op.drop_constraint('fk_student_id', 'attendance', type_='foreignkey')
        op.drop_constraint('fk_classroom_id', 'attendance', type_='foreignkey')
        op.drop_constraint('fk_subject_id', 'attendance', type_='foreignkey')
        op.drop_table('attendance')
