from models import *
from fastapi import FastAPI, HTTPException

app = FastAPI()

db: List[Student] = [
    Student(first_name="Raju",
            last_name="Agarwal", 
            gender=Gender.male, 
            sports_played=[SportsPlayed.badminton, SportsPlayed.basketball]), 
    
    Student(first_name='Addu', 
            last_name='Basha', 
            gender=Gender.male, 
            ), 
    
    Student(first_name='Prerna', 
            last_name='Pasham', 
            gender=Gender.female, 
            sports_played=[SportsPlayed.badminton]),
    
    Student(first_name="Touseef", 
            last_name="Uddin", 
            gender=Gender.male, 
            sports_played=[SportsPlayed.golf]), 
    
    Student(first_name='Shivek',
            last_name='Agarwal',
            gender=Gender.male,
            sports_played=[SportsPlayed.tt])
]

# assigning the roll no here
for student in db:
    student.assign_roll_no()
    
    
# api to get all the students
@app.get('/students/')
def get_students():
    return db

# api to get one student via roll no
@app.get('/students/{id}')
def get_student_by_id(id: int):
    for student in db:
        if student.roll_no == id:
            return student
    raise HTTPException(
        status_code=404,
        detail= f"The roll number {id} you are looking for is not found"
    )
    
# api to create a new student
@app.post('/create-student/')
def create_new_student(student: Student):
    if len(db)>=5:
        raise HTTPException(status_code=400, 
                            detail="Only 5 members are allowed in the cohort")
    student.assign_roll_no()
    db.append(student)
    return student

# api to delete a student
@app.delete('/delete-student/{roll_no}')
def delete_student(roll_no:int):
    for student in db:
        if student.roll_no == roll_no:
            db.remove(student)
            return {'message':f'deleted the student will roll no {roll_no}'}
    raise HTTPException(
        status_code=404,
        detail="invalid roll no"
    )
    
@app.put('/update-student/{roll_no}')
def update_student(roll_no: int, updated_student: Student):
    for student in db:
        if student.roll_no == roll_no:
            student.first_name = updated_student.first_name
            student.last_name = updated_student.last_name
            student.sports_played = updated_student.sports_played
            
            return student
        
    raise HTTPException(
        status_code=404,
        detail='student not found'
    )