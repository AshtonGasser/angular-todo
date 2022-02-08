#import {Task} from '../app/Task.ts' 
from sqlalchemy import Boolean, Column, String, Integer, DateTime

from datetime import datetime
from .entity import Entity, Base


class Task(Entity, Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    day = Column(DateTime)
    description = Column(String)
    reminder = Boolean(True)


    def __init__(self, text, day, description, reminder=True):
        Entity.__init__(self )
        self.text = text
        self.day = day
        self.description = description
        self.reminder = reminder