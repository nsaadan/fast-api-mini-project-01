#main.py

from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base
from db.base import Base 



def create_tables():   
	print('hi')       
	Base.metadata.create_all(bind=engine)
        
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	#app.include_router()
	create_tables()
	return app

app = start_application()