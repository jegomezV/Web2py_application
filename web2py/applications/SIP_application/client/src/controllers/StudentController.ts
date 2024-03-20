/* StudentController.ts */

// Import necessary classes
import { StudentModel } from '../models/StudentModel';
import { StudentRepository } from '../repository/StudentRepository';
import { StudentFactory } from '../factory/StudentFactory';

// Define the StudentController class
export class StudentController {
  // Declare private variables for the repository and factory
  private repository: StudentRepository;
  private factory: StudentFactory;

  // Constructor for the StudentController class
  constructor(repository: StudentRepository, factory: StudentFactory) {
    this.repository = repository;
    this.factory = factory;
  }

  // Method to register a student
  async registerStudent(name: string, email: string): Promise<StudentModel> {
    // Create a new student using the factory
    const student = this.factory.create(name, email);

    // Register the student using the repository
    const response = await this.repository.registerStudent(student);

    // If the registration was successful, return the student
    if (response.ok) {
      return student;
    } else {
      // If the registration was not successful, throw an error
      throw new Error('The user has already been created'); // Assume the error details include a "message" property
    }
  }
}
