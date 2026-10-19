
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

# Store study sessions in memory
study_sessions = []


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>My Study Tracker</title>
        </head>
        <body>
            <h1>My Study Tracker</h1>

            <p>Welcome! Use this application
            to track your study sessions.</p>

            <h2>Subjects I can study</h2>
            <ul>
                <li>Python</li>
                <li>FastAPI</li>
                <li>Machine Learning</li>
            </ul>

            <p>Your study tracker is running!</p>
        </body>
    </html>
    """


@app.get("/start-study")
def start_study(subject: str = "Python"):
    start_time = datetime.now()

    session = {
        "subject": subject,
        "start_time": start_time.isoformat()
    }

    study_sessions.append(session)

    return {
        "message": f"Started studying {subject}",
        "start_time": start_time.strftime("%H:%M:%S")
    }


@app.get("/study-history")
def study_history():
    return {
        "total_sessions": len(study_sessions),
        "sessions": study_sessions
    }
