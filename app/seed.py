from config import session
from models import Department, Student, Teacher

def seed_departments(session):
    # Create Department objects and add them to the session
    computer_dept = Department(name="Computer", location="Annex A")
    mathematics_dept = Department(name="Mathematics", location="Gurus Hall")
    english_dept = Department(name="English", location="Dreams Hall")
    history_dept = Department(name="History", location="Wazito Hall")
    chemistry_dept = Department(name="Chemistry", location="Annex")

    # Add departments to the session
    session.add_all([computer_dept, mathematics_dept, english_dept, history_dept, chemistry_dept])
    session.commit()

def seed_students(session):
    # Create Student objects and add them to the session
    levis = Student(name="Levis", age=20, gender="Male", email="levisrabah@gmail.com", phone="07895454", teacher_id=1)
    janet = Student(name="Janet Rafiki", age=22, gender="Female", email="jane@gmail.com", phone="07897654", teacher_id=1)
    meshack = Student(name="Meshack Kipchirchir", age=19, gender="Male", email="chirchir@gmail.com", phone="078934213", teacher_id=2)
    samuel = Student(name="Samuel Waweru", age=21, gender="Male", email="swaweru@gmail.com", phone="07324567", teacher_id=2)
    stayce = Student(name="Stayce Tracy", age=23, gender="Female", email="tracy@example.com", phone="0745123456", teacher_id=3)

    # Add students to the session
    session.add_all([levis, janet, meshack, samuel, stayce])
    session.commit()

def seed_teachers(session):
    # Query departments by name instead of using find_by_name
    computer_science_dept = session.query(Department).filter_by(name="Computer").first()
    mathematics_dept = session.query(Department).filter_by(name="Mathematics").first()
    english_dept = session.query(Department).filter_by(name="English").first()
    history_dept = session.query(Department).filter_by(name="History").first()
    chemistry_dept = session.query(Department).filter_by(name="Chemistry").first()

    # Create Teacher objects and add them to the session
    kevin = Teacher(name="Kevin Mkali", subject="Programming", department_id=computer_science_dept.id)
    martial = Teacher(name="Martial Munene", subject="Algorithms", department_id=computer_science_dept.id)
    wyclif = Teacher(name="Wyclif Bazuu", subject="Calculus", department_id=mathematics_dept.id)
    juddie = Teacher(name="Juddie Juliana", subject="Literature", department_id=english_dept.id)
    frank = Teacher(name="Frank Faulu", subject="World History", department_id=history_dept.id)
    grace = Teacher(name="Grace Gikonyo", subject="Organic Chemistry", department_id=chemistry_dept.id)


    # Add teachers to the session
    session.add_all([kevin, martial, wyclif, juddie, frank, grace])
    session.commit()

def seed_data():
    seed_departments(session)
    seed_students(session)
    seed_teachers(session)

if __name__ == "__main__":
    seed_data()
    print("Database seeded 👍️")
