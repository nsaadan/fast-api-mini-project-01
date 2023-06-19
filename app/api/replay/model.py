from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Replay(Base):
    id = Column(Integer,primary_key = True, index=True)
    replay = Column(String, nullable=False)
    tweet_id = Column(Integer, ForeignKey("tweet.id"))
    tweet = relationship("Tweet",back_populates="likes")
    # owner_id =  Column(Integer,ForeignKey("user.id"))
    # owner = relationship("User",back_populates="replays")


