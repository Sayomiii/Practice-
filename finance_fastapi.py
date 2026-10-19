
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

# Our temporary expense records
expenses = []

# Set a monthly budget in naira
monthly_budget = 50000


@app.get("/", response_class=HTMLResponse)
def home():
    total_spent = sum(
        expense["amount"] for expense in expenses
    )
    if total_spent > 50000:
        return f"""
        <html>
            <head>
                <title>My Expense Tracker</title>
            </head>
            <body>
                <h1>My Expense Tracker</h1>

                <h2 style="color: red;">Warning: You have exceeded your monthly budget!</h2>

                <h2>Monthly Budget: ₦{monthly_budget:,}</h2>
                <h2>Total Spent: ₦{total_spent:,}</h2>

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
    remaining = monthly_budget - total_spent

    return f"""
    <html>
        <head>
            <title>My Expense Tracker</title>
        </head>
        <body>
            <h1>My Expense Tracker</h1>

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


@app.get("/add-expense")
def add_expense(
    item: str,
    amount: float,
    category: str = "Other"
):
    if amount <= 0:
        return {"error": "Amount must be greater than zero"}

    expense = {
        "item": item,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
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
        "remaining_budget": monthly_budget - total_spent
    }
