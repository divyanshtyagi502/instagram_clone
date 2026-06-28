from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserProfile, UserResponse, UserLogin
from app.core.security import hash_password
from app.schemas.token import Token
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.post import Post
from app.schemas.post import PostResponse
router = APIRouter()


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = (
        db.query(User).filter(User.email==form_data.username).first()
    )
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    access_token = create_access_token(
        data={"sub": db_user.email}
    )
    return Token(access_token=access_token, token_type="bearer"
)

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = (
        db.query(User).filter(User.email==user.email).first()
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{user_id}", response_model=UserProfile)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    posts_count = len(existing_user.posts)
    followers_count = len(existing_user.followers)
    following_count = len(existing_user.following)
    return UserProfile(
        id=existing_user.id,
        username=existing_user.username,
        email=existing_user.email,
        posts_count=posts_count,
        followers_count=followers_count,
        following_count=following_count
    ) 
    
@router.get("/{user_id}/posts", response_model=list[PostResponse])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    posts = db.query(Post).filter(Post.owner_id == user_id).order_by(Post.created_at.desc()).all()
    return posts    
