def subjects_view():
    grid = SQLFORM.grid(db.subjects)
    return dict(grid=grid)
