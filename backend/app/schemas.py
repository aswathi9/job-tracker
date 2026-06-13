from pydantic import BaseModel, Field
from datetime import date  
from typing import Optional


class ApplicationCreate(BaseModel):
    company: str
    role: str
    joburl: Optional[str] = None
    status: str = "applied"
    current_round: Optional[str] = None
    interview_date: Optional[date] = None
    date_applied: date= Field(default_factory=date.today)
