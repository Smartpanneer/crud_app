from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Integer,String,Column
from database import Base,engine,sessionlocal
from table import Student
from schema import Student_update

app=FastAPI()



Base.metadata.create_all(bind=engine)

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()




#Create student
@app.get('/')
def home():
    return {'Message':'Wellcome to the crud app'}
@app.post('/students/')
def create_student(name:str,age:int,grade:str,db:Session=Depends(get_db)):
    new_stu=Student(name=name,age=age,grade=grade)
    db.add(new_stu)
    db.commit()
    db.refresh(new_stu)
    return new_stu
#read student
@app.get('/students/')
def get_student(db:Session=Depends(get_db)):
    return db.query(Student).all()
@app.get("/students/{student_id}")
def get_student_id(student_id:int,db:Session=Depends(get_db)):
    student= db.query(Student).filter(Student.id==student_id).first()

    if student:
        return student
    return {"Error":'Student not found'}

@app.put("/student/{student_id}")
def stu_update(student_id:int,request:Student_update,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(status_code=404,detail='Student not found')

    if request.name is not None:
        student.name=request.name
    if request.age is not None:
        student.age=request.age
    if request.grade is not None:
        student.grade=request.grade
    db.commit()
    db.refresh(student)

    return student
@app.delete('/student/{student_id}')
def delete(student_id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(status_code=404,detail='Student not found')

    db.delete(student)
    db.commit()
    return {'message':'Successfully delete the record'}