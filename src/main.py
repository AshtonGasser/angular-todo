from .entities.entity import Session, engine, Base
from .entities.tasks import Task
from flask import Flask, jsonify
from flask_cors import CORS


# creating the Flask application
app = Flask(__name__)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
tasks = session.query(Task).all()

if len(tasks) == 0:
    python_task = Task("SQLAlchemy Task", "Create a task", "script")
    session.add(python_task)
    session.commit()
    session.close()

    # reload tasks

    tasks = session.query(Task).all()

    # show existing tasks

    print('### Tasks:')
    for task in tasks:
        print(f'({task.id}) {task.title} - {task.day}')

