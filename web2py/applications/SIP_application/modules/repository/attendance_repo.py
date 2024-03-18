#attendance repository
from typing import Optional, Dict
from gluon import HTTP

class AttendanceRepository:
    """
    AttendanceRepository is a class that provides methods to interact with the 'attendance' collection in the database.
    """

    def __init__(self, db):
        """
        Initializes a new instance of the AttendanceRepository class.
        """
        self.db = db

    def get_all_attendance_repo(self):
        """
        Retrieves all attendance records from the 'attendance' collection.

        :return: A list of dictionaries representing the attendance records.
        """
        return self.db(self.db.attendance).select()

    def get_attendance_by_id_repo(self, attendance_id: int) -> Optional[dict]:
        """
        Retrieves an attendance record by its ID from the 'attendance' collection.

        :param attendance_id: An integer representing the attendance record's ID.
        :return: A dictionary representing the attendance record if found, None otherwise.
        :raises ValueError: If no attendance record is found with the provided ID.
        """
        attendance = self.db.attendance(attendance_id)
        if not attendance:
            raise ValueError(f"No attendance record found with id {attendance_id}")
        return attendance

    def update_attendance_repo(self, db, student_name: str, subject_name: str, classroom_name: str, attendance_status: str) -> Optional[dict]:
        """
        Inserts a new attendance record in the 'attendance' collection.

        :param student_name: A string representing the student's name.
        :param subject_name: A string representing the subject's name.
        :param classroom_name: A string representing the classroom's name.
        :param attendance_status: A string representing the attendance status.
        :return: A dictionary representing the inserted attendance record if successful, None otherwise.
        :raises ValueError: If any of the parameters are empty.
        """
        if not student_name or not subject_name or not classroom_name or not attendance_status:
            raise ValueError("All parameters are required")

        # Get the IDs of the student, subject, and classroom
        student = db(db.students.name == student_name).select().first()
        if student is None:
            raise ValueError(f"No student found with name {student_name}")
        student_id = student.id

        subject = db(db.subjects.name == subject_name).select().first()
        if subject is None:
            raise ValueError(f"No subject found with name {subject_name}")
        subject_id = subject.id

        classroom = db(db.classrooms.name == classroom_name).select().first()
        if classroom is None:
            raise ValueError(f"No classroom found with name {classroom_name}")
        classroom_id = classroom.id

        # Insert a new record in the 'attendance' table
        attendance_id = db.attendance.insert(
            student_id=student_id,
            subject_id=subject_id,
            classroom_id=classroom_id,
            status=attendance_status
        )

        return db.attendance(attendance_id)

    def delete_attendance_repo(self, attendance_id: int) -> bool:
        """
        Deletes an attendance record from the 'attendance' collection.

        :param attendance_id: An integer representing the attendance record's ID.
        :return: True if the deletion was successful, False otherwise.
        """
        return self.db.attendance(attendance_id).delete_record()
