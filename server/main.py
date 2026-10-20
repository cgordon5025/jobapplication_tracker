from fastapi import FastAPI
from routes.applications import router as applications_router
from database import Base, engine
from models.application_model import ApplicationModel
Base.metadata.create_all(bind=engine)
app = FastAPI();

app.include_router(applications_router)

@app.get("/")
def home():
    return {"message":"Job tracker is running"}