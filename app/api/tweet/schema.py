from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class TweetBase(BaseModel):
    text: Optional[str] = None
    created_at: Optional[date] = datetime.now().date()


class TweetCreate(TweetBase):
    text: str


class ShowTweet(TweetBase):
    text: str
    created_at: date

    class Config:
        orm_mode = True
