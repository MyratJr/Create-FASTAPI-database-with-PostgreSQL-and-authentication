from fastapi import APIRouter,Depends,HTTPException,status
from database import*
from models import*
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from jose import jwt
from typing import Annotated
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

router=APIRouter()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

@router.post('/token',tags=['login'])
async def login(user:Annotated[OAuth2PasswordRequestForm,Depends()],db:Session=Depends(get_db)):
    ret=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password",headers={"WWW-Authenticate": "Bearer"})
    q=db.query(Users).filter(Users.username==user.username).first()
    if not q or not pwd_context.verify(user.password,q.hashed_password):
        raise ret
    access_token=timedelta(hours=5,minutes=10)
    data={'sub':q.username}
    access_token=access_token+datetime.utcnow()
    print(access_token)
    data.update({'exp':access_token})
    encoded_jwt=jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
    return {'access_token':encoded_jwt,'token_type':'bearer'}