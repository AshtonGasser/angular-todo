from datetime import datetime
from sqlalchemy import Boolean, create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'tasks'
db_user = 'ashtongasser'
db_password = '0NLIN3-task'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    reminder = Column(Boolean)
  

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

   
       