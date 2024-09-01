from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the database models
class Student(db.Model):
    __tablename__ = 'Student'
    User_Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    DOB = db.Column(db.Date)
    Gender = db.Column(db.String(10))
    Fathers_Name = db.Column(db.String(100))
    Fathers_Education = db.Column(db.String(100))
    Fathers_Occupation = db.Column(db.String(100))
    Mothers_Name = db.Column(db.String(100))
    Mothers_Education = db.Column(db.String(100))
    Mothers_Occupation = db.Column(db.String(100))
    Language = db.Column(db.String(50))

class StudentActivity(db.Model):
    __tablename__ = 'Student_Activity'
    User_Id = db.Column(db.Integer, db.ForeignKey('Student.User_Id'), primary_key=True)
    Activity_Id = db.Column(db.Integer, db.ForeignKey('Activities.Activity_Id'), primary_key=True)
    Date = db.Column(db.Date)
    Month = db.Column(db.String(20))
    Grade = db.Column(db.String(2))

class Teacher(db.Model):
    __tablename__ = 'Teacher'
    User_Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Gender = db.Column(db.String(10))

class TeacherActivity(db.Model):
    __tablename__ = 'Teacher_Activity'
    User_Id = db.Column(db.Integer, db.ForeignKey('Teacher.User_Id'), primary_key=True)
    Activity_Id = db.Column(db.Integer, db.ForeignKey('Activities.Activity_Id'), primary_key=True)

class Activities(db.Model):
    __tablename__ = 'Activities'
    Activity_Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(255))
    Outcome = db.Column(db.String(100))
    Grade_1 = db.Column(db.String(2))
    Grade_2 = db.Column(db.String(2))
    Grade_3 = db.Column(db.String(2))
    Grade_4 = db.Column(db.String(2))
    Grade_5 = db.Column(db.String(2))
    Educational = db.Column(db.Boolean)

class Role(db.Model):
    __tablename__ = 'Role'
    Role_Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))

class Persona(db.Model):
    __tablename__ = 'Persona'
    User_Id = db.Column(db.Integer, primary_key=True)
    Role_Id = db.Column(db.Integer, db.ForeignKey('Role.Role_Id'))
    Password = db.Column(db.String(255))

# Create all tables
with app.app_context():
    db.create_all()

# Functions to add data to each table
def add_student(data):
    student = Student(**data)
    db.session.add(student)
    db.session.commit()

def add_student_activity(data):
    student_activity = StudentActivity(**data)
    db.session.add(student_activity)
    db.session.commit()

def add_teacher(data):
    teacher = Teacher(**data)
    db.session.add(teacher)
    db.session.commit()

def add_teacher_activity(data):
    teacher_activity = TeacherActivity(**data)
    db.session.add(teacher_activity)
    db.session.commit()

def add_activity(data):
    activity = Activities(**data)
    db.session.add(activity)
    db.session.commit()

def add_role(data):
    role = Role(**data)
    db.session.add(role)
    db.session.commit()

def add_persona(data):
    persona = Persona(**data)
    db.session.add(persona)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
