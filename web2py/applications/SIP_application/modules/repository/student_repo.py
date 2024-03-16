from typing import Optional, List

class StudentRepository:
    """
    StudentRepository is a class that provides methods to interact with the 'students' collection in the database.
    """

    def __init__(self, db):
        """
        Initializes a new instance of the StudentRepository class.

        """
        self.db = db

    def get_all_students(self) -> List[dict]:
        """
        Retrieves all students from the 'students' collection.

        :return: A list of dictionaries representing the students.
        """
        return self.db.students.select()

    def get_student_by_id(self, student_id: int) -> Optional[dict]:
        """
        Retrieves a student by its ID from the 'students' collection.

        :param student_id: An integer representing the student's ID.
        :return: A dictionary representing the student if found, None otherwise.
        :raises ValueError: If no student is found with the provided ID.
        """
        student = self.db.students(student_id)
        if not student:
            raise ValueError(f"No student found with id {student_id}")
        return student

    def create_student(self, name: str, email: str) -> dict:
        """
        Creates a new student in the 'students' collection.

        :param name: A string representing the student's name.
        :param email: A string representing the student's email.
        :return: A dictionary representing the created student.
        :raises ValueError: If either 'name' or 'email' is empty.
        """
        if not name or not email:
            raise ValueError("Both name and email are required")
        return self.db.students.insert(name=name, email=email)

    def update_student(self, student_id: int, name: str, email: str) -> Optional[dict]:
        """
        Updates a student in the 'students' collection.

        :param student_id: An integer representing the student's ID.
        :param name: A string representing the student's name.
        :param email: A string representing the student's email.
        :return: A dictionary representing the updated student if successful, None otherwise.
        :raises ValueError: If either 'name' or 'email' is empty.
        """
        if not name or not email:
            raise ValueError("Both name and email are required")
        return self.db.students(student_id).update_record(name=name, email=email)

    def delete_student(self, student_id: int) -> bool:
        """
        Deletes a student from the 'students' collection.

        :param student_id: An integer representing the student's ID.
        :return: True if the deletion was successful, False otherwise.
        """
        return self.db.students(student_id).delete_record()
