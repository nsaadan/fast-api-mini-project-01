from sqlalchemy.orm import Session
from .schema import TweetCreate
from .model import Tweet


def create_new_tweet(tweet: TweetCreate, db: Session, owner_id:int):
    tweet_object = Tweet(**tweet.dict(),owner_id=owner_id)
    db.add(tweet_object)
    db.commit()
    db.refresh(tweet_object)
    return tweet_object


def retreive_tweet(id:int,db:Session):
    item = db.query(Tweet).filter(Tweet.id == id).first()
    return item

def list_tweets(db : Session):  
    tweets = db.query(Tweet).all()
    return tweets


def update_tweet(id:int, tweet: TweetCreate, db: Session, owner_id:int):
    existing_tweet = db.query(Tweet).filter(Tweet.id == id)
    if not existing_tweet.first():
        return 0
    tweet.__dict__.update(owner_id=owner_id)
    existing_tweet.update(tweet.__dict__)
    db.commit()
    return 1


def delete_tweet(id: int,db: Session,owner_id:int):
    existing_tweet = db.query(Tweet).filter(Tweet.id == id)
    if not existing_tweet.first():
        return 0
    existing_tweet.delete(synchronize_session=False)
    db.commit()
    return 1