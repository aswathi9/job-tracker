from pydantic import BaseModel
from datetime import date  


class ApplicationCreate(BaseModel):
    company: str
    role: str
    joburl: str | None= None
    status: str = "applied"
    current_round: str | None= None
    interview_date: date | None= None
    date_applied: date
