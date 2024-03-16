from typing import Dict

class StudentFactory:
    """
    A factory class for creating students.

    Attributes:
        db: A database connection object.
    """

    def __init__(self, db: object) -> None:
        """
        The constructor for StudentFactory class.

        Parameters:
            db (object): A database connection object.
        """
        self.db = db

    def create_student(self, name: str, email: str) -> Dict[str, str]:
        """
        The function to create a student.

        Parameters:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            dict: A dictionary containing the name and email of the student.
        """
        # Here you can add any additional logic you need for creating a student
        return self.db.students.insert(name=name, email=email)
