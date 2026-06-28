from pydantic import BaseModel, EmailStr
from app.schemas.user import UserPublic
class PostCreate(BaseModel):
    caption: str
    image_url: str
    
class PostResponse(BaseModel):
    id: int
    caption: str
    image_url: str
    owner: UserPublic
    likes_count: int
    comments_count: int
    
    
    model_config = {
        "from_attributes": True
    }