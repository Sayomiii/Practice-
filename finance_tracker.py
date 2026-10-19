
from http.client import HTTPException
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone
from pydantic import BaseModel, Field
"""
datetime -> lets you obtain the current date and time.
timezone -> lets you work with
HTMLResponse tells FastAPI that a response should be served as HTML, so the browser renders it as a webpage rather than displaying it as ordinary text. time zones, including UTC.
Pydantic helps you validate data entering your application.
BaseModel -> lets you define the structure of the data you expect.
Field -> lets you specify validation rules for individual fields.
"""

app = FastAPI(title="Personal Expense Tracker")
'''
FastAPI(title="Personal Expense Tracker") -> Creates a FastAPI application instance with the title "Personal Expense Tracker".
'''
# Our temporary expense records, data disappears when the server restarts.
expenses = []

# Set a monthly budget in naira
monthly_budget = 50000

class ExpenseCreate(BaseModel):
    item: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(default="Other", min_length=1, max_length=50)
'''
A class -> is a blueprint for creating objects or defining a structure.
ExpenseCreate -> describes the data format expected when someone sends a POST request to create an expense.
BaseModel -> is provided by Pydantic. By inheriting from it, your class gains automatic data parsing and validation.
'''


@app.get("/", response_class=HTMLResponse)
# The @app.get("/") decorator defines a route for the root URL ("/") of the application. When a user accesses this URL, the home() function is called to handle the request.
    
def home():
    total_spent = sum(
        expense["amount"] for expense in expenses
        #Take the expenses and get its amount
    )
    remaining = monthly_budget - total_spent
    #this calculates the remaining budget by subtracting the total spent from the monthly budget.
    warning_message = ""
    if total_spent > monthly_budget:
        warning_message = "<h2 style='color: red;'>Warning: You have exceeded your monthly budget!</h2>"
    return f"""
    <html>
        <head>
            <title>My Expense Tracker</title>
        </head>
        <body>
            <h1>My Expense Tracker</h1>
            {warning_message}
            <h2>Monthly Budget: ₦{monthly_budget:,}</h2>
            <h2>Total Spent: ₦{total_spent:,}</h2>
            <h2>Remaining: ₦{remaining:,}</h2>

            <p>Number of expenses: {len(expenses)}</p>

            <h3>Actions</h3>
            <p>
                <a href="/add-expense?item=Lunch&amount=2500&category=Food">
                    Record a sample lunch expense
                </a>
            </p>
        
            <p>
                <a href="/expense-history">
                    View expense history
                </a>
            </p>
        </body>
    </html>
    """

#This registers a GET endpoint at /add-expense.
@app.get("/add-expense")
def add_expense(
    item: str,
    amount: float,
    category: str = "Other"
):
    if amount <= 0:
        raise HTTPException(
            status_code=400,
           detail="Amount must be greater than zero"
           )
        

    expense = {
        "id": len(expenses) + 1,
        "item": item,
        "amount": amount,
        "category": category,
        "date": datetime.now(timezone.utc).isoformat()
    }

    '''
    datetime.now(...) -> obtains the current date and time.
    timezone.utc -> specifies UTC.
    .isoformat() -> converts the datetime object into a standard text representation.
    '''

    expenses.append(expense)

    return {
        "message": "Expense recorded successfully",
        "expense": expense
    }



# 3. NEW GET endpoint: retrieve all expenses
#-This registers a GET endpoint at /expenses. 
#The URL is: http://127.0.0.1:8000/expenses



@app.get("/expenses")
def get_expenses():
    return {
        "count": len(expenses),
        "expenses": expenses}

@app.post("/expenses", status_code=201)
def create_expense(expense: ExpenseCreate):
    expense =  {
        "id": len(expenses) + 1,
        "item": expense.item,
        "amount": expense.amount,
        "category": expense.category,
        "date": datetime.now(timezone.utc).isoformat()
    }
    expenses.append(expense)
    return {
        "message": "Expense recorded successfully",
        "expense": expense
    }

@app.get("/expense-history")
def expense_history():
    total_spent = sum(
        expense["amount"] for expense in expenses
    )

    return {
        "expenses": expenses,
        "total_spent": total_spent,
        "monthly_budget": monthly_budget,
        "remaining_budget": monthly_budget - total_spent,
        "budget_exceeded": total_spent > monthly_budget
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Expense Tracker",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
@app.get("/health/ready")
def readiness_check():
    return {
        "status": "ready",
        "message": "Application is ready to accept requests."
    }