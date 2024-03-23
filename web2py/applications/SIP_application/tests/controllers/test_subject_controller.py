import unittest
from unittest.mock import patch, Mock
from applications.SIP_application.controllers.subjects import subjects_view

class TestSubjectsView(unittest.TestCase):
    @patch('applications.SIP_application.controllers.subjects.SQLFORM')
    @patch('applications.SIP_application.controllers.subjects.db')
    @patch('applications.SIP_application.controllers.subjects.request')
    @patch('applications.SIP_application.controllers.subjects.response')
    def test_subjects_view(self, mock_response, mock_request, mock_db, mock_sqlform):
        mock_sqlform.grid.return_value = 'grid'
        mock_response.generic_patterns = []
        mock_request.env = Mock(web2py_runtime_gae=False)  # Change this line
        result = subjects_view()
        self.assertIsInstance(result, dict)
        self.assertIn('grid', result)
        self.assertEqual(result['grid'], 'grid')

if __name__ == '__main__':
    unittest.main()
    