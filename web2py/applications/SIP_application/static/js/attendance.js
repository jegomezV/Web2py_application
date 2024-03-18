async function updateAttendance(selectElement) {
    try {
        var row = selectElement.parentNode.parentNode;
        var studentName = row.children[0].innerText;
        var subjectName = row.children[1].innerText;
        var classroomName = row.children[2].innerText;
        var attendanceStatus = selectElement.value;

        var data = {
            student: studentName,
            subject: subjectName,
            classroom: classroomName,
            attendance: attendanceStatus
        };

        const response = await fetch('http://127.0.0.1:8000/SIP_application/attendance/update_attendance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const responseData = await response.json();

        console.log('Success:', responseData);
    } catch (error) {
        console.error('Error:', error);
    }
}

function addEventListeners() {
    // Agrega un event listener a todos los controles select de asistencia
    document.querySelectorAll('.attendance-select').forEach((select) => {
        select.addEventListener('change', (event) => {
            // Llama a la función updateAttendance cuando se cambie el estado en el control select
            updateAttendance(event.target);
        });
    });
}

window.onload = function() {
    // Aquí debes agregar el HTML al DOM
    // ...

    // Luego, llama a la función addEventListeners
    addEventListeners();
};
