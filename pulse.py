from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from typing import Literal

app = FastAPI()
AnalysisTask = Literal["sentiment", "summary"]


class SentimentResult(BaseModel):
    label:Literal["positive", "negative", "neutral"]
    score:float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score for the sentiment analysis",
    )


class AnalysisResponse(BaseModel):
    sentiment: SentimentResult | None = None
    summary: str | None = None


class AnalysisRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1000, description="Text to analyze")
    tasks:list[AnalysisTask] = Field(
        min_length=1,
        description="List of analysis tasks to perform",
    )

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty")
        return value


@app.post("/analysis/text", response_model=AnalysisResponse)
def analysis_text(request: AnalysisRequest):
    return {
        "sentiment": {
            "label": "positive",
            "score": 0.95,
        }
    }
        
    
