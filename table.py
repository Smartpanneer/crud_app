from sqlalchemy import Integer,String,Column
from database import Base

class Student(Base):
    __tablename__='student'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    age=Column(Integer)
    grade=Column(String(20))
