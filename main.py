from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator


app = FastAPI()
@app.get("/")
def home ():
    return {"message": "Pulse Analysis is running"}

class AnalysisRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1000, description="Text to analyze")

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty")
        return value

@app.post("/analyze/text")
def analyze_text(request: AnalysisRequest):
    return{
        "sentiment":"positive",
        "recieved_text": request.text
    }
