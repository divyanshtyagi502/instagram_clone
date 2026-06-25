from fastapi import FastAPI

app = FastAPI(title="Instagram Clone MVP")

@app.get("/")
def root():
    return {"message": "Welcome to the Instagram Clone MVP!"}