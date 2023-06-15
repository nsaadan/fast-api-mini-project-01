from fastapi import APIRouter
from api.user import router as user_router
from api.tweet import router as tweet_router
from api.auth import router as login_router


api_router = APIRouter()
api_router.include_router(user_router.router,prefix="/users",tags=["users"])
api_router.include_router(tweet_router.router,prefix="/tweets",tags=["tweets"])
api_router.include_router(login_router.router,prefix="/login",tags=["login"])  
