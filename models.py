from database import base
from sqlalchemy import Column, Integer, String, Float

class Users(base):
    __tablename__='Users'

    id=Column(Integer,primary_key=True)
    username=Column(String(8))
    hashed_password=Column(String)
    email=Column(String)


class Products(base):
    __tablename__='Products'

    id=Column(Integer, primary_key=True)
    name=Column(String(50))
    description=Column(String)
    price=Column(Float)