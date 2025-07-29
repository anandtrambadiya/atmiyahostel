from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db, Student, Assembly, Attendance
from datetime import datetime
from datetime import date as dt_date, timedelta

main_blueprint = Blueprint('main', __name__)

ADMIN_USERNAME = 'atmiya'
ADMIN_PASSWORD = 'au2025'

HOSTEL_OPTIONS = ["All", "NIRAMAY", "SARVANAMAN", "MUNJKA"]

@main_blueprint.route('/')
def dashboard():
    today = dt_date.today()
    cutoff_date = today - timedelta(days=1)

    active_assemblies = Assembly.query.filter(Assembly.date >= cutoff_date).order_by(Assembly.date.asc()).all()
    past_assemblies = Assembly.query.filter(Assembly.date < cutoff_date).order_by(Assembly.date.desc()).all()

    return render_template('dashboard.html',
                            active_assemblies=active_assemblies,
                            past_assemblies=past_assemblies,
                            today=today,
                            cutoff_date=cutoff_date)


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@main_blueprint.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('main.login'))

@main_blueprint.before_request
def require_login():
    # List of routes you can visit without being logged in
    allowed_routes = ['main.login', 'static']
    if request.endpoint not in allowed_routes and not session.get('admin_logged_in'):
        return redirect(url_for('main.login'))

@main_blueprint.route('/assembly/create', methods=['GET', 'POST'])
def create_assembly():
    if request.method == 'POST':
        title = request.form['title']
        assembly_date_str = request.form['date']
        speaker = request.form.get('speaker')

        try:
            assembly_date = datetime.strptime(assembly_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Please enter a valid date.')
            return render_template('create_assembly.html')

        if assembly_date < dt_date.today():
            flash('Assembly date cannot be in the past.')
            return render_template('create_assembly.html')

        new_assembly = Assembly(title=title, date=assembly_date, speaker=speaker)
        db.session.add(new_assembly)
        db.session.commit()
        flash('Assembly created successfully!')
        return redirect(url_for('main.dashboard'))
    
    return render_template('create_assembly.html', current_date=dt_date.today().isoformat())


@main_blueprint.route('/assembly/<int:assembly_id>/attendance', methods=['GET', 'POST'])
def take_attendance(assembly_id):
    assembly = Assembly.query.get_or_404(assembly_id)

    # Get filter inputs from URL query parameters or defaults
    hostel_filter = request.args.get('hostel_filter', 'All')
    room_search = request.args.get('room_no', '').strip()

    # Build query with filters applied
    query = Student.query

    if hostel_filter != "All":
        query = query.filter(Student.hostel == hostel_filter)

    if room_search:
        query = query.filter(Student.room_no.like(f'%{room_search}%'))

    # Order by hostel, then room_no, then student name for grouping in template
    students = query.order_by(Student.hostel, Student.room_no, Student.name).all()

    if request.method == 'POST':
        # Collect the set of student IDs marked present (checkbox names)
        present_student_ids = set(request.form.keys())

        for student in students:
            record = Attendance.query.filter_by(assembly_id=assembly.id, student_id=student.id).first()
            if not record:
                record = Attendance(assembly_id=assembly.id, student_id=student.id)
                db.session.add(record)
            record.present = str(student.id) in present_student_ids
        db.session.commit()

        flash('Attendance saved successfully!')
        # Redirect to the same page preserving filters
        return redirect(url_for('main.take_attendance', assembly_id=assembly.id,
                                hostel_filter=hostel_filter, room_no=room_search))

    # For GET: load existing attendance data for this assembly
    attendance_records = {a.student_id: a.present for a in Attendance.query.filter_by(assembly_id=assembly.id)}

    return render_template('take_attendance.html',
                           assembly=assembly,
                           students=students,
                           attendance=attendance_records,
                           hostel_options=HOSTEL_OPTIONS,
                           selected_hostel=hostel_filter,
                           room_search=room_search)

