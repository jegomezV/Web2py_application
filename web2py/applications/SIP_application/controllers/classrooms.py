def classrooms_view():
    grid_classroom = SQLFORM.grid(db.classrooms, orderby=db.classrooms.name, paginate=4)
    return dict(grid=grid_classroom)
