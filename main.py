from fastapi import FastAPI

app = FastAPI();

@app.get("/")
def home():
    return {"message":"Job tracker is running"}

@app.get("/applications")
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