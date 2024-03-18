import logging
from gluon import XML

class Renderer:
    def __init__(self):
        # Configura el logging
        logging.basicConfig(filename='app.log', level=logging.DEBUG)
        self.logger = logging.getLogger('sampleLogger')


    def render_attendance(self, data):
        self.logger.debug('Starting render_attendance')

        html = '<table style="width: 100%; table-layout: auto; border-collapse: separate; border-spacing: 2em;">\n'
        html += '<tr><th>Student</th><th>Subject</th><th>Classroom</th><th>Attendance</th></tr>\n'
        for row in data:
            self.logger.debug(f'Rendering row for student {row["student"]["name"]}')
            html += '<tr>'
            html += f'<td>{row["student"]["name"]}</td>'
            html += f'<td>{row["subject"]["name"]}</td>'
            html += f'<td>{row["classroom"]["name"]}</td>'
            html += f'<td><select name="attendance-{row["student"]["name"]}" class="attendance-select" data-id="{row["student"]["name"]}">'
            html += '<option value="" selected>Seleccionar</option>'
            html += '<option value="attended">Asistió</option>'
            html += '<option value="absent">Ausente</option>'
            html += '</select></td>'
            html += '</tr>\n'

        self.logger.debug('Finished render_attendance')
        html += '</table>'
        return XML(html)