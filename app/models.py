from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    head = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # One-to-many relationship: One department can have many teachers
    teachers = relationship("Teacher", back_populates='department')

    def __repr__(self):
        return f"<Department(id={self.id}, name={self.name}, location={self.location}, head={self.head})>"

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Foreign key to relate a student to a teacher
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)

    # Many-to-one relationship: Many students can have one teacher
    teacher = relationship("Teacher", back_populates='students')

    def __repr__(self):
        return (f"<Student(id={self.id}, name='{self.name}', age={self.age}, "
                f"gender='{self.gender}', email='{self.email}', phone='{self.phone}', "
                f"teacher_id={self.teacher_id})>")


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    gender = Column(String, nullable=False) 
    created_at = Column(DateTime, default=datetime.utcnow)

    # Foreign key to relate a teacher to a department
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    # One-to-many relationship: One teacher can have many students
    students = relationship("Student", back_populates='teacher')

    # Many-to-one relationship: Many teachers belong to one department
    department = relationship("Department", back_populates='teachers')

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', subject='{self.subject}', gender='{self.gender}', department_id={self.department_id})>"