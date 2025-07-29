from app import app
from models import db, Student

students = [
    # NIRAMAY students 1-18
    {"hostel": "NIRAMAY", "room_no": "1", "name": "Student1"},
    {"hostel": "NIRAMAY", "room_no": "1", "name": "Student2"},
    {"hostel": "NIRAMAY", "room_no": "1", "name": "Student3"},
    {"hostel": "NIRAMAY", "room_no": "1", "name": "Student4"},
    {"hostel": "NIRAMAY", "room_no": "1", "name": "Student5"},
    {"hostel": "NIRAMAY", "room_no": "1", "name": "Student6"},
    {"hostel": "NIRAMAY", "room_no": "2", "name": "Student7"},
    {"hostel": "NIRAMAY", "room_no": "2", "name": "Student8"},
    {"hostel": "NIRAMAY", "room_no": "2", "name": "Student9"},
    {"hostel": "NIRAMAY", "room_no": "2", "name": "Student10"},
    {"hostel": "NIRAMAY", "room_no": "2", "name": "Student11"},
    {"hostel": "NIRAMAY", "room_no": "2", "name": "Student12"},
    {"hostel": "NIRAMAY", "room_no": "3", "name": "Student13"},
    {"hostel": "NIRAMAY", "room_no": "3", "name": "Student14"},
    {"hostel": "NIRAMAY", "room_no": "3", "name": "Student15"},
    {"hostel": "NIRAMAY", "room_no": "3", "name": "Student16"},
    {"hostel": "NIRAMAY", "room_no": "3", "name": "Student17"},
    {"hostel": "NIRAMAY", "room_no": "3", "name": "Student18"},

    # SARVANAMAN students 19-34
    {"hostel": "SARVANAMAN", "room_no": "1", "name": "Student19"},
    {"hostel": "SARVANAMAN", "room_no": "1", "name": "Student20"},
    {"hostel": "SARVANAMAN", "room_no": "1", "name": "Student21"},
    {"hostel": "SARVANAMAN", "room_no": "1", "name": "Student22"},
    {"hostel": "SARVANAMAN", "room_no": "1", "name": "Student23"},
    {"hostel": "SARVANAMAN", "room_no": "1", "name": "Student24"},
    {"hostel": "SARVANAMAN", "room_no": "2", "name": "Student25"},
    {"hostel": "SARVANAMAN", "room_no": "2", "name": "Student26"},
    {"hostel": "SARVANAMAN", "room_no": "2", "name": "Student27"},
    {"hostel": "SARVANAMAN", "room_no": "2", "name": "Student28"},
    {"hostel": "SARVANAMAN", "room_no": "2", "name": "Student29"},
    {"hostel": "SARVANAMAN", "room_no": "2", "name": "Student30"},
    {"hostel": "SARVANAMAN", "room_no": "3", "name": "Student31"},
    {"hostel": "SARVANAMAN", "room_no": "3", "name": "Student32"},
    {"hostel": "SARVANAMAN", "room_no": "3", "name": "Student33"},
    {"hostel": "SARVANAMAN", "room_no": "3", "name": "Student34"},

    # MUNJKA students 35-50
    {"hostel": "MUNJKA", "room_no": "1", "name": "Student35"},
    {"hostel": "MUNJKA", "room_no": "1", "name": "Student36"},
    {"hostel": "MUNJKA", "room_no": "1", "name": "Student37"},
    {"hostel": "MUNJKA", "room_no": "1", "name": "Student38"},
    {"hostel": "MUNJKA", "room_no": "1", "name": "Student39"},
    {"hostel": "MUNJKA", "room_no": "1", "name": "Student40"},
    {"hostel": "MUNJKA", "room_no": "2", "name": "Student41"},
    {"hostel": "MUNJKA", "room_no": "2", "name": "Student42"},
    {"hostel": "MUNJKA", "room_no": "2", "name": "Student43"},
    {"hostel": "MUNJKA", "room_no": "2", "name": "Student44"},
    {"hostel": "MUNJKA", "room_no": "2", "name": "Student45"},
    {"hostel": "MUNJKA", "room_no": "2", "name": "Student46"},
    {"hostel": "MUNJKA", "room_no": "3", "name": "Student47"},
    {"hostel": "MUNJKA", "room_no": "3", "name": "Student48"},
    {"hostel": "MUNJKA", "room_no": "3", "name": "Student49"},
    {"hostel": "MUNJKA", "room_no": "3", "name": "Student50"},
]

with app.app_context():
    db.session.bulk_save_objects([Student(**s) for s in students])
    db.session.commit()
    print('Seeded 50 students across NIRAMAY, SARVANAMAN, and MUNJKA')
