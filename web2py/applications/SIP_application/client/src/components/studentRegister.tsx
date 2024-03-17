// Import React and useState hook
import React, { useState } from 'react';

// Define an interface for the Student
interface Student {
    name: string;
    email: string;
}

// Define the StudentRegister component
const StudentRegister = () => {
    // Use the useState hook to manage the student state
    const [student, setStudent] = useState<Student>({ name: '', email: '' });
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [error, setError] = useState<string | null>(null);

    // Define the handleInputChange function
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setStudent({ ...student, [name]: value });
    };

    // Define the handleSubmit function
const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    // Reset the isSubmitted and error states
    setIsSubmitted(false);
    setError(null);

    // Validation for empty fields
    if (!student.name || !student.email) {
        alert('Please fill in all fields');
        return;
    }

    // Additional validation for the username
    if (student.name.length < 3) {
        alert('The username must be at least 3 characters long');
        return;
    }

    // Additional validation for the email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(student.email)) {
        alert('Please enter a valid email');
        return;
    }

    // API call
    try {
        const response = await registerStudent(student);
    
        if (!response.ok) {
            throw new Error(`The user has already been created`);
        }
    
        setIsSubmitted(true);

    } catch (error) {
        if (error instanceof Error) {
            setError(error.message);
        } else {
            console.error(error);
        }
    }
};

    // Render the component
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
};

// Function to register a student
async function registerStudent(student: Student) {
    return await fetch('http://127.0.0.1:8000/SIP_application/students/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(student)
    });
}

// Export the StudentRegister component
export default StudentRegister;