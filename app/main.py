from config import *


def exit_program():
    """Exit the program with a farewell message."""
    print("Welcome Again! 🙋️")
    session.close()  # Close the session when exiting
    exit()

# ----------------------------
# Department Functions
# ----------------------------
def list_departments():
    """List all departments."""
    departments = session.query(Department).all()
    if not departments:
        print("No departments found.")
    else:
        for department in departments:
            print(department)

def find_department_by_name():
    """Find a department by name."""
    name = input("Enter department name: ").strip()
    department = session.query(Department).filter(Department.name == name).first()
    if department:
        print(department)
    else:
        print(f"No department found with the name '{name}'.")

def find_department_by_id():
    """Find a department by ID."""
    department_id = int(input("Enter department ID: "))
    department = session.query(Department).filter(Department.id == department_id).first()
    if department:
        print(department)
    else:
        print(f"No department found with the ID '{department_id}'.")

def create_department():
    """Create a new department."""
    name = input("Enter department name: ").strip()
    location = input("Enter department location: ").strip()
    head = input("Enter department head: ").strip()
    department = Department(name=name, location=location, head=head)
    session.add(department)
    session.commit()
    print(f"Department created: {department}")

def update_department():  
    """Update an existing department."""
    department_id = int(input("Enter department ID: "))
    department = session.query(Department).filter(Department.id == department_id).first()
    if department:
        name = input(f"Enter new name (current: {department.name}): ").strip() or None
        location = input(f"Enter new location (current: {department.location}): ").strip() or None
        head = input(f"Enter new head (current: {department.head}): ").strip() or None
        if name: department.name = name
        if location: department.location = location
        if head: department.head = head
        session.commit()
        print(f"Department updated: {department}")
    else:
        print(f"No department found with the ID '{department_id}'.")

def delete_department():
    """Delete a department."""
    department_id = int(input("Enter department ID: "))
    department = session.query(Department).filter(Department.id == department_id).first()
    if department:
        session.delete(department)
        session.commit()
        print(f"Department deleted: {department}")
    else:
        print(f"No department found with the ID '{department_id}'.")

# ----------------------------
# Student Functions
# ----------------------------
def list_students():
    """List all students."""
    students = session.query(Student).all()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def find_student_by_name():
    """Find a student by name."""
    name = input("Enter student name: ").strip()
    student = session.query(Student).filter(Student.name == name).first()
    if student:
        print(student)
    else:
        print(f"No student found with the name '{name}'.")

def find_student_by_id():
    """Find a student by ID."""
    student_id = int(input("Enter student ID: "))
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        print(student)
    else:
        print(f"No student found with the ID '{student_id}'.")

def create_student():
    """Create a new student."""
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    gender = input("Enter student gender: ").strip()
    email = input("Enter student email: ").strip()
    phone = input("Enter student contact: ").strip()
    teacher_id = int(input("Enter teacher ID: "))
    student = Student(name=name, age=age, gender=gender, email=email, phone=phone, teacher_id=teacher_id )
    session.add(student)
    session.commit()
    print(f"Student created: {student}")

def update_student():
    """Update an existing student."""
    student_id = int(input("Enter student ID: "))
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        name = input(f"Enter new name (current: {student.name}): ").strip() or None
        age = input(f"Enter new age (current: {student.age}): ").strip()
        gender = input(f"Enter new gender (current: {student.gender}): ").strip() or None
        email = input(f"Enter new email (current: {student.email}): ").strip() or None
        phone = input(f"Enter new contact (current: {student.phone}): ").strip() or None
        teacher_id = input(f"Enter new teeacher ID (current: {student.teacher_id}): ").strip() or None

        if name: student.name = name
        if age: student.age = int(age)
        if gender: student.gender = gender
        if email: student.email = email
        if phone: student.phone = phone
        if teacher_id: student.teacher_id = int(teacher_id)

        session.commit()
        print(f"Student updated: {student}")
    else:
        print(f"No student found with the ID '{student_id}'.")

def delete_student():
    """Delete a student."""
    student_id = int(input("Enter student ID: "))
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student deleted: {student}")
    else:
        print(f"No student found with the ID '{student_id}'.")

# ----------------------------
# Teacher Functions
# ----------------------------
def list_teachers():
    """List all teachers."""
    teachers = session.query(Teacher).all()
    if not teachers:
        print("No teachers found.")
    else:
        for teacher in teachers:
            print(teacher)

def find_teacher_by_name():
    """Find a teacher by name."""
    name = input("Enter teacher name: ").strip()
    teacher = session.query(Teacher).filter(Teacher.name == name).first()
    if teacher:
        print(teacher)
    else:
        print(f"No teacher found with the name '{name}'.")

def find_teacher_by_id():
    """Find a teacher by ID."""
    teacher_id = int(input("Enter teacher ID: "))
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        print(teacher)
    else:
        print(f"No teacher found with the ID '{teacher_id}'.")

def create_teacher():
    """Create a new teacher."""
    name = input("Enter teacher name: ").strip()
    gender = input("Enter teacher gender: ").strip()
    subject = input("Enter teacher subject: ").strip()
    department_id = int(input("Enter department ID: "))
    teacher = Teacher(name=name, gender=gender, subject=subject,  department_id=department_id)
    session.add(teacher)
    session.commit()
    print(f"Teacher created: {teacher}")

def update_teacher():
    """Update an existing teacher."""
    teacher_id = int(input("Enter teacher ID: "))
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        name = input(f"Enter new name (current: {teacher.name}): ").strip() or None
        gender = input(f"Enter new gender (current: {teacher.gender}): ").strip() or None
        subject = input(f"Enter new subject (current: {teacher.subject}): ").strip() or None
        department_id = input(f"Enter new department ID (current: {teacher.department_id}): ").strip() or None

        if name: teacher.name = name
        if gender: teacher.gender = gender
        if subject: teacher.subject = subject
        if department_id: teacher.department_id = int(department_id)

        session.commit()
        print(f"Teacher updated: {teacher}")
    else:
        print(f"No teacher found with the ID '{teacher_id}'.")

def delete_teacher():
    """Delete a teacher."""
    teacher_id = int(input("Enter teacher ID: "))
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher deleted: {teacher}")
    else:
        print(f"No teacher found with the ID '{teacher_id}'.")

def list_department_teachers():
    """List all teachers in a department."""
    department_id = int(input("Enter the department ID: "))
    department = session.query(Department).filter(Department.id == department_id).first()
    if department:
        for teacher in department.teachers:
            print(teacher)
    else:
        print(f"No department found with the ID '{department_id}'.")


# ----------------
# Main CLI App
# ----------------

def main():
    while True:
        os.system('clear')
        print("Welcome to Tech School")
        print("1. Manage Departments")
        print("2. Manage Teachers")
        print("3. Manage Students")
        print("4. exit")
        main_menu_choice = input("Enter your choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. List Departments")
                print("2. Find Department by Name")
                print("3. Find Department by Id")
                print("4. Create Department")
                print("5. update Department")
                print("6. Delete Department")
                print("7. Back to Main Menu")
                department_menu_choice = input("Enter your choice: ")
                if department_menu_choice == '1':
                    list_departments()
                elif department_menu_choice == '2':
                    find_department_by_name()
                elif department_menu_choice == '3':
                    find_department_by_id()
                elif department_menu_choice == '4':
                    create_department()
                elif department_menu_choice == '5':
                    update_department() 
                elif department_menu_choice == '6':
                    delete_department()
                elif department_menu_choice == '7':
                    break
                input("Press Enter to continue...")


        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. List Teacher")
                print("2. Find Teacher by Name")
                print("3. Find Teacher by Id")
                print("4. Create Teacher")
                print("5. Update Teacher")
                print("6. Delete Teacher")
                print("7. List Deparment Teachers")
                print("8. Back to Main Menu")
                teacher_menu_choice = input("Enter your choice: ")
                if teacher_menu_choice == '1':
                    list_teachers()
                elif teacher_menu_choice == '2':
                    find_teacher_by_name()
                elif teacher_menu_choice == '3':
                    find_teacher_by_id()
                elif teacher_menu_choice == '4':
                    create_teacher()
                elif teacher_menu_choice == '5':
                    update_teacher()
                elif teacher_menu_choice == '6':
                    delete_teacher()
                elif teacher_menu_choice == '7':
                    list_department_teachers()
                elif teacher_menu_choice == '8':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. List Students")
                print("2. Find Student By Name")
                print("3. Find Student By Id")
                print("4. Create student")
                print("5. Update Student")
                print("6. Delete Student")
                print("7. Back to Main Menu")
                student_menu_choice = input("Enter your choice: ")
                if student_menu_choice == '1':
                    list_students()
                elif student_menu_choice == '2':
                    find_student_by_name()
                elif student_menu_choice == '3':
                    find_student_by_id()
                elif student_menu_choice == '4':
                    create_student()
                elif student_menu_choice == '5':
                    update_student()
                elif student_menu_choice == '6':
                    delete_student()
                elif student_menu_choice == '7':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '4':
                exit_program()

        else:
            print("Invalid choice! Please choice again.")
            input("Press Enter to continue...")


# call the main function
main()
                
