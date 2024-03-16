from typing import Dict, Any
from ...factory.student_fact import StudentFactory
from ...repository.student_repo import StudentRepository

def create_student(student_data: Dict[str, str], db: Any):
    """
    Create a student object using the factory and insert the student data into the database.

    Args:
        student_data (Dict[str, str]): A dictionary containing student data. It should have 'name' and 'email' keys.
        db (Any): Database connection object.

    Returns:
        Student: An instance of the Student class.
    """
    # Create the student object using the factory
    student_factory = StudentFactory(db)
    student = student_factory.create_student(student_data['name'], student_data['email'])

    # Insert the student data into the database
    student_repository = StudentRepository(db)
    student_repository.create_student(student.name, student.email)

    return student
