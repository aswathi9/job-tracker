from fastapi import FastAPI
from app.schemas import ApplicationCreate
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Job tracker api is running"}

@app.post("/applications/")
def create_application(application: ApplicationCreate):
    return application