from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Tweet(Base):
    id = Column(Integer,primary_key = True, index=True)
    text = Column(String,nullable=False)
    created_at = Column(Date)
    retweet = Column(Integer, default=0)
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("User",back_populates="tweets")
    likes = relationship("Like",back_populates="tweet")
    replays = relationship("Replay",back_populates="tweet")




