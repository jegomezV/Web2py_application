"""
This module contains the controller for student operations. 
It includes functions for viewing and registering students.
"""

from http import HTTPStatus
from gluon import HTTP
from applications.SIP_application.modules.services.business_logic.student_service import create_student

def students_view():
    # Obtén los estudiantes de la base de datos
    response.view = 'students_view.html'
    return {'message': 'Students view'}