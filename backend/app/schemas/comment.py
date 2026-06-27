from datetime import datetime
from pydantic import BaseModel


class CommentCreate(BaseModel):
    content: str


class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    user_id: int
    post_id: int

    class Config:
        from_attributes = True