from fastapi import APIRouter,Depends,HTTPException,status
from database import Session
from schema import*
from models import*
from passlib.context import CryptContext
from typing import Annotated

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()


from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post('/create_user',response_model=CrUser)
async def create_user(user:CrUser_,db:Session=Depends(get_db)):
    before=db.query(Users).filter(Users.email==user.email).first()
    if before:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='User already exists')
    newUser=Users(username=user.username,email=user.email,hashed_password=pwd_context.hash(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return {'username':user.username,'email':user.email}

@router.delete('/delete_user/{id}')
async def delete_user(id:int,db:Session=Depends(get_db)):
    will_delete_user=db.get(Users,id)
    if not will_delete_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User Not Found')
    db.delete(will_delete_user)
    db.commit()
    return {'detail':'User deleted'}

@router.post('/create_p')
async def create_products(product:CrApSc,db:Session=Depends(get_db)):
    new_product=Products(name=product.name,description=product.description,price=product.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.put('/update_p/{id}',response_model=CrApSc)
async def update_product(id:int,new_info:CrApSc,db:Session=Depends(get_db)):
    a=db.get(Products,id)
    if not a:
        raise HTTPException(status_code=404, detail='Product Not Found')
    b=new_info.dict(exclude_unset=True)
    for key, value in b.items():
        setattr(a,key,value)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a

@router.delete('/delete_p/{id}')
async def delete_product(id:int,db:Session=Depends(get_db)):
    del_=db.get(Products, id)
    db.delete(del_)
    db.commit()
    return {'detail':'Product Deleted'}