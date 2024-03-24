/* formEvents.ts */

import { StudentModel } from './src/models/StudentModel';
import { StudentRepository } from './src/repository/StudentRepository';
import { StudentFactory } from './src/factory/StudentFactory';
import { FormRenderer } from './src/renderer/FormRenderer';

const repository = new StudentRepository();
const factory = new StudentFactory();
const renderer = new FormRenderer();
 
document.addEventListener('DOMContentLoaded', () => {
  // Render the form
const studentsTable = document.getElementById('students-table');
if (studentsTable) {
    studentsTable.innerHTML = renderer.render();
}

const form = document.querySelector('#student-registration-form');
if (form) {
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const form = event.target as HTMLFormElement;
        const name = (form.elements.namedItem('name') as HTMLInputElement).value;
        const email = (form.elements.namedItem('email') as HTMLInputElement).value;

        try {
            const student = factory.create(name, email);
            await repository.registerStudent(student);
            console.log('Student registered:', student);
        } catch (error) {
            console.error('Error registering student:', error);
        }
    });
}
});