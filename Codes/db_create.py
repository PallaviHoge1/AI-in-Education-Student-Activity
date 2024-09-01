from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initial connection to MySQL server without specifying a database
engine = create_engine('mysql+mysqlconnector://root:root@localhost', echo=True)

# Create the database if it doesn't exist
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS StudentActivityDB;"))

# Define the database connection parameters
DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/StudentActivityDB'

# Create an engine that stores data in the specified database URI
engine = create_engine(DATABASE_URI, echo=True)

# Declare a base for the database models
Base = declarative_base()

# Define the database models
class Student(Base):
    __tablename__ = 'Student'
    User_Id = Column(Integer, primary_key=True)
    Name = Column(String(100))
    DOB = Column(Date)
    Gender = Column(String(10))
    Fathers_Name = Column(String(100))
    Fathers_Education = Column(String(100))
    Fathers_Occupation = Column(String(100))
    Mothers_Name = Column(String(100))
    Mothers_Education = Column(String(100))
    Mothers_Occupation = Column(String(100))
    Language = Column(String(50))

class Activities(Base):
    __tablename__ = 'Activities'
    Activity_Id = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Description = Column(String(255))
    Outcome = Column(String(100))
    Grade_1 = Column(String(200))
    Grade_2 = Column(String(200))
    Grade_3 = Column(String(200))
    Grade_4 = Column(String(200))
    Grade_5 = Column(String(200))
    Educational = Column(String(200))

class StudentActivity(Base):
    __tablename__ = 'Student_Activity'
    User_Id = Column(Integer, ForeignKey('Student.User_Id'), primary_key=True)
    Activity_Id = Column(Integer, ForeignKey('Activities.Activity_Id'), primary_key=True)
    Date = Column(Date)
    Month = Column(String(20))
    Grade = Column(String(2))

class Teacher(Base):
    __tablename__ = 'Teacher'
    User_Id = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Gender = Column(String(10))

class TeacherActivity(Base):
    __tablename__ = 'Teacher_Activity'
    User_Id = Column(Integer, ForeignKey('Teacher.User_Id'), primary_key=True)
    Activity_Id = Column(Integer, ForeignKey('Activities.Activity_Id'), primary_key=True)

class Role(Base):
    __tablename__ = 'Role'
    Role_Id = Column(Integer, primary_key=True)
    Name = Column(String(50))

class Persona(Base):
    __tablename__ = 'Persona'
    User_Id = Column(Integer, primary_key=True)
    Role_Id = Column(Integer, ForeignKey('Role.Role_Id'))
    Password = Column(String(255))

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)
print("Database and tables created successfully.")
