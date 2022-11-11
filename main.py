from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative  import declarative_base

from dotenv import load_dotenv
import os
# load config values as env variables
load_dotenv()

# config for the database
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
pwd = os.getenv('DB_PASSWORD')

# connect to the database engine
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/postgres', echo=False)
# bind session to the engine
Session = sessionmaker(bind=engine)
session = Session()

# Base Class
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

#Create the table
Base.metadata.create_all(engine)

"""Adding data to a table in the database"""
s1 = Student(name="Shubhushan", age=22, grade="Bachelor")
s2 = Student(name="Shambhu", age=22, grade="tenth")
s3 = Student(name="aabhushan", age=15, grade="tenth")

session.add_all([s1, s2, s3])

session.commit()
session.close()

def print_students(db_obj):
    for student in db_obj:
        print(f"{student.name}, {student.age}")
"""Fetching values from the database"""
#all data of in the students table
students = session.query(Student)
print_students(students)

#order the rows according to name
print("Ordered Data:")
students = session.query(Student).order_by(Student.name)
print_students(students)

#filter data
student = session.query(Student).filter(Student.name=="aabhushan").first()
print("Filtered Data:")
print(student.name)
students = session.query(Student).filter(or_(Student.name=="aabhushan", Student.name=="Shambhu"))
print_students(students)

#total count of rows in the table
students = session.query(Student).count()
print(students)

"""Updating the values in the database"""
student = session.query(Student).filter(Student.name=="Shambhu").first()
student.name = "shambhu"
student.age = 23
session.commit()

"""Delete data in the database"""
student = session.query(Student).filter(Student.name == "shambhu").first()
session.delete(student)
session.commit()
