# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
from applications.SIP_application.modules.repository.student_repo import StudentRepository
from applications.SIP_application.modules.services.business_logic import student_service

# Create an instance of StudentRepository
student_repository = StudentRepository(db)

# ---- example index page ----
def index():
    response.flash = T("SIP")
    return dict(message=T('SIP'))

def register_student():
    """Registers a new student."""

    if request.env.request_method != 'POST':
        raise HTTP(HTTPStatus.METHOD_NOT_ALLOWED)

    try:
        # Print request details for debugging
        print('request.env:', request.env)

        # Extract student data from the request vars
        # Create an instance of StudentService

        student_data = request.vars

        # Check if student_data is None
        if student_data is None:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Student data not provided')

        # Validate student data
        if 'name' not in student_data or not student_data['name']:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Name is required')
        if 'email' not in student_data or not student_data['email']:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Email is required')

        print("CONTROLLERRR")
        # Create student and save in the database
        student_service.create_student(student_data, db)

        # Return success message
        return dict(success=True, message="Student registered successfully")
    except Exception as e:
        raise HTTP(400, "controller error " + str(e)) from e


# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
