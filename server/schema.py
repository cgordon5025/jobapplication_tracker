# schemas.py
from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    name: str
    website: str | None = None