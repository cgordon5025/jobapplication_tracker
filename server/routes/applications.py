from fastapi import APIRouter

router = APIRouter();

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