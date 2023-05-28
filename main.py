from fastapi import FastAPI, Depends
from models import*
from database import engine
from schema import*
import client, user, login
from login import oauth2_scheme

base.metadata.create_all(bind=engine)


app=FastAPI()
app.include_router(login.router,tags=['login'])
app.include_router(client.router,tags=['clients'])
app.include_router(user.router,tags=['users'],dependencies=[Depends(oauth2_scheme)])