from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from typing import List
from db.session import get_db
from .model import Tweet
from .schema import TweetCreate, ShowTweet
from .service import (
    create_new_tweet,
    retreive_tweet,
    list_tweets,
    update_user_tweet,
    delete_user_tweet,
    list_user_tweets,
)
from api.user.model import User
from api.auth.router import get_current_user_from_token

router = APIRouter()


@router.post("/create-tweet/", response_model=ShowTweet)
def create_tweet(
    tweet: TweetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    tweet = create_new_tweet(tweet=tweet, db=db, owner_id=current_user.id)
    return tweet


@router.get("/get/{id}", response_model=ShowTweet)
def read_tweet(id: int, db: Session = Depends(get_db)):
    tweet = retreive_tweet(id=id, db=db)
    if not tweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tweet with this id {id} does not exist",
        )
    return tweet


@router.get("/user-tweet/{id}", response_model=List[ShowTweet])
def read_user_tweet(id: int, db: Session = Depends(get_db)):
    tweets = list_user_tweets(id=id, db=db)
    if not tweets:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} doesnt have any tweets",
        )
    return tweets


@router.get("/all", response_model=List[ShowTweet])
def read_all_tweet(db: Session = Depends(get_db)):
    tweets = list_tweets(db=db)
    return tweets


@router.put("/update/{id}")
def update_tweet(
    id: int,
    create: TweetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    tweet = retreive_tweet(id=id, db=db)
    if not tweet:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tweet with {id} does not exist",
        )
    if tweet.owner_id == current_user.id:
        update_user_tweet(id=id, tweet=create, db=db, owner_id=current_user.id)
        return {"msg": "Successfully updated."}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail=f"You are not permitted!"
    )


@router.delete("/delete/{id}")
def delete_tweet(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    tweet = retreive_tweet(id=id, db=db)
    if not tweet:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tweet with {id} does not exist",
        )
    if tweet.owner_id == current_user.id:
        delete_user_tweet(id=id, db=db, owner_id=current_user.id)
        return {"msg": "Successfully deleted."}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail=f"You are not permitted!"
    )
