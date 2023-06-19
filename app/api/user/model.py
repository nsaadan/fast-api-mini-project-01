from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    hashed_password = Column(String,nullable=False)
    tweets = relationship("Tweet",back_populates="owner")
    # likes = relationship("Like",back_populates="owner")
    # replays = relationship("Replay",back_populates="onwer")

    # follwing x followers * 2 * relationship
    



