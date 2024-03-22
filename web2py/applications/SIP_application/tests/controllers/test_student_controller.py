import applications.SIP_application.controllers.students as students
import unittest
from unittest.mock import Mock, patch
from http import HTTPStatus

class TestStudentsController(unittest.TestCase):
    def setUp(self):
        self.request = Mock()
        students.request = self.request

    @patch('applications.SIP_application.modules.services.business_logic.student_service.create_student')
    def test_register_student_success(self, mock_create_student):
        self.request.env.request_method = 'POST'
        self.request.vars = {'name': 'Test Student', 'email': 'test@student.com'}

        response = students.register()

        mock_create_student.assert_called_once_with(self.request.vars, students.db)
        self.assertEqual(response, {'success': True})

    def test_register_student_bad_request(self):
        self.request.env.request_method = 'POST'
        self.request.vars = None

        with self.assertRaises(HTTP) as context:
            students.register()

        self.assertEqual(context.exception.status, HTTPStatus.BAD_REQUEST)

    def test_register_student_method_not_allowed(self):
        self.request.env.request_method = 'GET'

        with self.assertRaises(HTTP) as context:
            students.register()

        self.assertEqual(context.exception.status, HTTPStatus.METHOD_NOT_ALLOWED)

if __name__ == '__main__':
    unittest.main()
