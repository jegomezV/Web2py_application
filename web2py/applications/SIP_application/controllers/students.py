import os

def students_view():
    return response.stream(os.path.join(request.folder, 'static', 'build', 'index.html'))