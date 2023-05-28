from fastapi import APIRouter,Depends,HTTPException,status
from database import Session
from schema import*
from models import*

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()

@router.get('/get_p/{id}')
async def get_product(id:int,db:Session=Depends(get_db)):
    prod=db.get(Products,id)
    if not prod:
        raise HTTPException(status_code=404,detail='Product Not Found')
    return prod

@router.get('/get_all_p',response_model=list[CrApSc])
async def get_all_product(db:Session=Depends(get_db)):
    return db.query(Products).all()