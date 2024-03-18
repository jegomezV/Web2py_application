#attendance controller
import json
from applications.SIP_application.modules.repository.student_repo import StudentRepository
from applications.SIP_application.modules.renderer.attendance_renderer import Renderer
from applications.SIP_application.modules.repository.attendance_repo import AttendanceRepository

def attendance():
    # Crea una instancia de StudentRepository
    student_repository = StudentRepository(db)

    # Obtén los datos de los estudiantes, materias y salones de la base de datos.
    students = student_repository.get_all_students()
    subjects = db(db.subjects).select()  # Obtiene todas las materias directamente de la base de datos
    classrooms = db(db.classrooms).select()  # Obtiene todos los salones directamente de la base de datos

    # Prepara los datos para el Renderer.
    data = []
    for student in students:
        for subject in subjects:
            for room in classrooms:
                data.append({
                    "student": {"name": student.name},
                    "subject": {"name": subject.name},
                    "classroom": {"name": room.name},
                })

    renderer = Renderer()
    attendance_table = renderer.render_attendance(data)

    return dict(attendance_table=attendance_table)

def show_attendance():
    attendance_table = attendance()
    return dict(attendance_table=attendance_table)

def update_attendance():
    # Recibe los datos de la solicitud
    data = request.body.read()
    data = json.loads(data) if data else None

    # Comprueba si data es None
    if data is None:
        raise HTTP(400, "No data provided")

    student_name = data.get('student')
    subject_name = data.get('subject')
    classroom_name = data.get('classroom')
    attendance_status = data.get('attendance')

    # Comprueba si alguno de los datos necesarios es None
    if None in [student_name, subject_name, classroom_name, attendance_status]:
        return dict(success=False, message="Missing data")

    # Crea una instancia de AttendanceRepository
    attendance_repository = AttendanceRepository(db)

    # Inserta un nuevo registro de asistencia en la base de datos
    success = attendance_repository.update_attendance_repo(db, student_name, subject_name, classroom_name, attendance_status)

    return dict(success=success)