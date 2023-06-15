#db >repository > login.py
from sqlalchemy.orm import Session

from api.user.model import User 


def get_user(username:str,db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user