from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://postgres:63365663@localhost/new"

engine=create_engine(DATABASE_URL)

Session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

base=declarative_base()