/* StudentRegister.ts */

// Import necessary classes
import React, { useState } from 'react';
import { StudentModel } from '../models/StudentModel';
import { StudentRepository } from '../repository/StudentRepository';
import { StudentFactory } from '../factory/StudentFactory';
import { StudentController } from '../controllers/StudentController';

// Component for student registration
export function StudentRegister() {
    const studentRepository = new StudentRepository();
    const studentFactory = new StudentFactory();
    const studentController = new StudentController(studentRepository, studentFactory);

    // Initialize student state
    const [student, setStudent] = useState<StudentModel>(studentFactory.create('', ''));
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [error, setError] = useState<string | null>(null);

    // Handle input change
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setStudent({ ...student, [name]: value });
    };

    // Handle form submission
    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        setIsSubmitted(false);
        setError(null);

        // Validate student name and email
        if (!student.name || !student.email) {
            alert('Please fill in all fields');
            return;
        }

        // Validate student name
        if (student.name.length < 3) {
            alert('The username must be at least 3 characters long');
            return;
        }

        // Validate student email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(student.email)) {
            alert('Please enter a valid email');
            return;
        }

        // Register student
        try {
            await studentController.registerStudent(student.name, student.email);
            setIsSubmitted(true);
            setStudent(studentFactory.create('', '')); // Reset the form
        } catch (error) {
            // Handle error
            if (error instanceof Error) {
                setError(error.message); // Display the error message from the server
            } else {
                console.error(error);
            }
        }
    };

    // Render component
    return (
        <main className="h-screen flex flex-col items-center justify-center">
            <h2 className="text-4xl mb-4 md:mb-6 font-bold hover:drop-shadow-[0_0_0.3rem_#ffffff70] text-gray-200 hover:duration-300 text-center duration-400">Student Register</h2>
            <div className='bg-gradient-to-b from-black from-75% to-violet-900 hover:duration-200 grid justify-items-center rounded-3xl py-6 md:py-5 shadow-md shadow-purple-600 border-[1px] hover:shadow-violet-500 hover:shadow-lg border-purple-950 w-full max-w-screen-lg mx-auto'>
                <form onSubmit={handleSubmit} className="space-y-4 md:space-y-3 p-4 md:p-6 w-full mx-auto">
                    <div className="text-sm mb-2">
                        <label>
                            Student name:
                            <input type="text" name="name" value={student.name} onChange={handleInputChange} className="block w-full mt-4 hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full" required />
                        </label>
                        <label>
                            Email:
                            <input type="email" name="email" value={student.email} onChange={handleInputChange} className="block w-full mt-4 hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full" required />
                        </label>
                    </div>
                    <button type="submit" className="block w-full mt-4 hover:drop-shadow-[0_0_0.1rem_#ffffff70] duration-400 p-2 md:p-1 text-center text-gray-300 md:text-[15px] hover:text-white border border-purple-400 shadow shadow-purple-950 hover:duration-300 hover:shadow-inner hover:shadow-purple-700 rounded-full">Register</button>
                    {isSubmitted && <p className="mt-4 text-center text-green-300">Student has been registered successfully!</p>}
                    {error && <p className="mt-4 text-center text-red-500">Error registering student: {error}</p>}
                </form>
            </div>
        </main>
    );
}
