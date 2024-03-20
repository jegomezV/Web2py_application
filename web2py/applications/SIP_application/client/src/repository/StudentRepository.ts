/* StudentRepository.ts */

// Import the StudentModel class
import { StudentModel } from '../models/StudentModel';

// Define the StudentRepository class
export class StudentRepository {
  // Method to register a student
  async registerStudent(student: StudentModel) {
    // Send a POST request to the server to register the student
    const response = await fetch(
      'http://127.0.0.1:8000/SIP_application/students/register',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        // Convert the student object to a JSON string
        body: JSON.stringify(student),
      },
    );

    // Return the response from the server
    return response;
  }
}
