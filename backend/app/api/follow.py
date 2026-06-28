from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.follow import Follow
from app.models.user import User
from app.core.auth import get_current_user

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.post("/{user_id}", status_code=201)
def follow_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if user_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    existing_follow = (
        db.query(Follow)
        .filter(Follow.follower_id == current_user.id, Follow.following_id == user_id)
        .first()
    )
    if existing_follow:
        raise HTTPException(status_code=400, detail="You are already following this user")

    new_follow = Follow(follower_id=current_user.id, following_id=user_id)
    db.add(new_follow)
    db.commit()
    return {"detail": "User followed successfully"}

@router.delete("/{user_id}", status_code=204)
def unfollow_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    follow = (
        db.query(Follow)
        .filter(Follow.follower_id == current_user.id, Follow.following_id == user_id)
        .first()
    )
    if not follow:
        raise HTTPException(status_code=404, detail="You are not following this user")

    db.delete(follow)
    db.commit()
    return {"detail": "User unfollowed successfully"}

@router.get("/followers/{user_id}")
def get_followers(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    followers = db.query(Follow).filter(
        Follow.following_id == user_id
    ).all()

    return {
        "count": len(followers),
        "followers": followers
    }
    
    
@router.get("/following/{user_id}")
def get_following(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    following = db.query(Follow).filter(
        Follow.follower_id == user_id
    ).all()

    return {
        "count": len(following),
        "following": following
    }