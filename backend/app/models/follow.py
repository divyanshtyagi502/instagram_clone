from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy.sql import func
from sqlalchemy import UniqueConstraint

class Follow(Base):
    __tablename__ = "follows"
    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    following_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    follower = relationship("User", foreign_keys=[follower_id], backref="following")
    followed = relationship("User", foreign_keys=[following_id], backref="followers")
    
    __table_args__ = (UniqueConstraint('follower_id', 'following_id', name='unique_follow'),)