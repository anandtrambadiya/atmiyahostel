# backend/routes/__init__.py
from .student_routes import student_bp

def register_routes(app):
    app.register_blueprint(student_bp, url_prefix='/api/students')
