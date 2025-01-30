from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class Student(BaseModel):
    id: int
    name: str
    grade: int
#ngj
students = [
        Student(id=1, name='karm', grade=5),
        Student(id=2,name='mona',grade=4),
 Student(id=3,name='sara',grade=1)
    ]


@app.get('/students/')
def read_students():
    return students

@app.post("/students/")
def create_student(New_Student:Student):
    students.append(New_Student)
    return New_Student

@app.put("/students/{student_id}")
def update_student(student_id:int, update_student:Student):
    for index, student in enumerate(students):
     if student.id==student_id:
        students[index]=update_student
        return update_student
    return{"error":"student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index, student in enumerate(students):
     if student.id==student_id:
        del students[index]
        return {"message":"student deleted"}
     return {"error":"student not found "}