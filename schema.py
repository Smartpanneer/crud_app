from pydantic import BaseModel
class Student_update(BaseModel):
    name:str|None=None
    age:int|None=None
    grade:str|None=None