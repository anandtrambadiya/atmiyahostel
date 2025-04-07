# backend/routes/student_routes.py
from flask import Blueprint, jsonify

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/')
def get_students():
    return jsonify({"students": ["Anand", "Ravi", "Prashnat"]})
