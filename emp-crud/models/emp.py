from pydantic import BaseModel

class Employee(BaseModel):
    eid:int
    ename:str 
    esal:float 
    gender:str