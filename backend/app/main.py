from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Instagram Clone MVP")

@app.get("/")
def root():
    return {"message": "Welcome to the Instagram Clone MVP!"}
