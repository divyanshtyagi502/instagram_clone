from pydantic import BaseModel, EmailStr

class PostCreate(BaseModel):
    caption: str
    image_url: str
    
class PostResponse(BaseModel):
    id: int
    caption: str
    image_url: str
    owner_id: int

    model_config = {
        "from_attributes": True
    }