from pydantic import BaseModel

class CrApSc(BaseModel):
    name:str
    description:str
    price:float

    class Config:
        orm_mode=True


class CrUser(BaseModel):
    username:str
    email:str

class CrUser_(CrUser):
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str