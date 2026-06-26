from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.core.auth import get_current_user
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostResponse

router = APIRouter(tags=["Posts"])

@router.post("/posts", response_model=PostResponse)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_post = Post(
        caption=post.caption,
        image_url=post.image_url,
        owner_id=current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post