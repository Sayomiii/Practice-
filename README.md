# Title 
Study Tracker API
## Description
A simple REST API built with Python and FastAPI to manage study assignments, track deadlines, monitor completion status, and summarize study progress.

## Project Overview
The Study Tracker API was developed to practise building RESTful APIs, handling HTTP requests, validating data with Pydantic, and implementing CRUD operations using FastAPI.

## Features

- Create study assignments with titles, descriptions, priorities, and deadlines.
- Retrieve all assignments.
- Mark assignments as completed.
- Delete assignments by ID.
- Generate a summary of assignment progress, including completed, pending, and overdue assignments.

## Toold
- Python: Core programming language.
- FastAPI: API framework.
- Pydantic: Request data validation using BaseModel.
- Python date: Handling assignment deadlines.
- Uvicorn: Development server.
- API Endpoints

## How it works

 Run the application
`` bash
uvicorn main:app --reload
``
## API 

The API will run locally at:
``bash
http://127.0.0.1:8000
``
## Explore the API documentation

To Open the interactive Swagger documentation in your browser:
``bash
http://127.0.0.1:8000/docs
``
## Conclusion

The Study Tracker API demonstrates the fundamentals of building and documenting a RESTful API with FastAPI. It provides a foundation for developing more advanced study-management applications with persistent storage, testing, and authentic