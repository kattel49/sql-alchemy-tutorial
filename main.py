from sqlalchemy import create_engine, Column, Integer, String
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

Base.metadata.create_all(engine)

s1 = Student(name="Shubhushan", age=22, grade="Bachelor")
session.add(s1)

session.commit()