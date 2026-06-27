from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.models.comment import Comment
from app.models.post import Post
from app.schemas.comment import CommentCreate, CommentResponse
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/posts/{post_id}", response_model=CommentResponse) 
def create_comment(post_id: int, comment: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    new_comment = Comment(content=comment.content, user_id=current_user.id, post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/posts/{post_id}", response_model=list[CommentResponse])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return comments

@router.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this comment")
    db.delete(comment)
    db.commit()
    return Response(status_code=204, content={"detail": "Comment deleted successfully"})