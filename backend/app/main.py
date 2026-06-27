from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.user import User
from app.models.post import Post
from app.api.user import router as user_router
from app.api.post import router as post_router
from app.api.comment import router as comment_router
from app.models.like import Like
from app.models.comment import Comment

print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Instagram Clone MVP")
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
@app.get("/")
def root():
    return {"message": "Welcome to the Instagram Clone MVP!"}
