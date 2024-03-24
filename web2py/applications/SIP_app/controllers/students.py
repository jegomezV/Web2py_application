"""
This module contains the controller for student operations. 
It includes functions for viewing and registering students.
"""

from http import HTTPStatus
from gluon import HTTP
from applications.SIP_application.modules.services.business_logic.student_service import create_student

def students_view():
    # Obtén los estudiantes de la base de datos
    return {'message': 'Students view'}

def register_student():
    """Registers a new student."""

    if request.env.request_method != 'POST':
        raise HTTP(HTTPStatus.METHOD_NOT_ALLOWED)

    try:
        # Print request details for debugging
        print('request.env:', request.env)

        # Extract student data from the request vars
        # Create an instance of StudentService

        student_data = request.vars

        # Check if student_data is None
        if student_data is None:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Student data not provided')

        # Validate student data
        if 'name' not in student_data or not student_data['name']:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Name is required')
        if 'email' not in student_data or not student_data['email']:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Email is required')

        print("CONTROLLERRR")
        # Create student and save in the database
        create_student(student_data, db)

        # Return success message
        return dict(success=True, message="Student registered successfully")
    except Exception as e:
        raise HTTP(400, "controller error " + str(e)) from e