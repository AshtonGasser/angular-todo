#import {Task} from '../app/Task.ts' 
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime

from datetime import datetime
from .entity import Entity, Base


class Task(Entity, Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    day = Column(DateTime)
    description = Column(String)
    reminder = True


    def __init__(self, title, day, description, created_by, reminder):
        Entity.__init__(self, created_by)
        self.title = title
        self.day = day
        self.description = description
        self.reminder = reminder