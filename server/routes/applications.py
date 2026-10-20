from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services.add_application import add_application
from schema import ApplicationCreate
router = APIRouter();


#connect to db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/applications")
def get_applications():
     return[
           {
                     "company": "Acme Technologies",
                     "role": "Software Engineer",
                     "status": "Applied"
                 },
                 {
                     "company": "Northstar Labs",
                     "role": "Backend Developer",
                     "status": "Interview"
                 }

     ]

@router.post("/new-app")
def new_application(
    application_data: ApplicationCreate,
    db:Session = Depends(get_db)
):
    return add_application(
        db=db,
        companyName = data.companyName,
        website = data.website,
        status = data.status
    )


#@router.update("/")