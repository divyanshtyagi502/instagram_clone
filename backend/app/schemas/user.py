from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
class UserPublic(BaseModel):
    id: int
    username: str    

class UserProfile(BaseModel):
    id: int
    username: str
    email: EmailStr
    
    posts_count: int
    followers_count: int
    following_count: int

    class Config:
        from_attributes = True