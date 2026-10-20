# schemas.py
from pydantic import BaseModel
from models.application_status_enum import ApplicationStatus
from datetime import datetime, date

class ApplicationCreate(BaseModel):
    name: str
    website: str | None = None
    status: ApplicationStatus = ApplicationStatus.APPLIED
    lastUpdated: date