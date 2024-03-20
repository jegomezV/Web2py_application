from typing import Dict, Any
from gluon import HTTP
from ...factory.student_fact import StudentFactory
from ...repository.student_repo import StudentRepository

def create_student(student_data: Dict[str, str], db: Any):
    """
    Create a student object using the factory and insert the student data into the database.

    Args:
        student_data (Dict[str, str]):
        A dictionary containing student data.
        It should have 'name' and 'email' keys.
        db (Any): Database connection object.

    Returns:
        Student: An instance of the Student class.
    """

    try:
        student_repository = StudentRepository(db)
        student_factory = StudentFactory()
        student = student_factory.create_student(student_data['name'], student_data['email'])
        student_repository.create_student_repo(student)
        return student

    except Exception as e:
        # Log the error and return it
        raise HTTP(400, "Error service " + str(e)) from e
