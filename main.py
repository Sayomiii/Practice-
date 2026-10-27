from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

#API SAVED

app = FastAPI(title="Study Tracker API", description="API for managing student records", version="1.0.0")

#Assign assigment

assignment=[]

#For the next assignment
next_assignment_id =1

#Defining the struture of the class CreateAssignment
class CreateAssignment(BaseModel):
    title: str
    subject: str
    deadline: date
    priority: str ="Medium"  # Default value for priority is "Medium"

#Creating an endpoint to welcome the students

@app.get('/')
def home ():
    return {"message": "Welcome to the Study Tracker API! Use the endpoints to manage your assignments."}

#Creating an endpoint to create an assignment with the required fields and validation for priority

@app.post('/assignments')
def create_assignment(assignment_data: CreateAssignment):
    global next_assignment_id


    if assignment_data.priority not in ["Medium", "High", "Low"]:
        raise HTTPException(status_code=400, detail="Invalid priority value. Must be 'Medium', 'High', or 'Low'.")

    assignment_entry = {
        "id": next_assignment_id,
        "title": assignment_data.title,
        "subject": assignment_data.subject,
        "deadline": assignment_data.deadline.isoformat(),
        "priority": assignment_data.priority,
        "completed": False
    }
    #Adding the assignment_entry to the list
    assignment.append(assignment_entry)


    #Increasing the id for the next assignment
    next_assignment_id += 1
    return {
        "message": "Assignment created succesffuly",
        "assignment": assignment_entry
    }


#Creating an endpoint to get the total number of assignments
@app.get('/assignments')
def get_assignments():
    return {
         "total_assignments": len(assignment)
        }
#Creating an endpoint to update the assignment status to completed

@app.patch('/assignments/{assignment_id}/completed')
def update_assignment(assignment_id: int, updated_assignment: CreateAssignment):
    for assignment_entry in assignment:
        if assignment_entry["id"] == assignment_id:
            assignment_entry["completed"] = True
            return {"message": "Assignment completed successfully", "assignment": assignment_entry}
        
    raise HTTPException(status_code=404, detail="Assignment not found")

#Creating an endpoint to delete an assignment by its ID
@app.delete('/assignments/{assignment_id}')
def delete_assignment(assignment_id: int):
    for assignment_entry in assignment:
        if assignment_entry["id"] == assignment_id:
            assignment.remove(assignment_entry)
            return {"message": "Assignment deleted successfully"}
        
    raise HTTPException(status_code=404, detail="Assignment not found")

""" Making sure all RESTAPI are used and defined"""