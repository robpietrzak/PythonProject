# models.py
# This file defines the database tables using SQLAlchemy models

from database import db

class Task(db.Model):
    # Primary key (unique ID for each task)
    id = db.Column(db.Integer, primary_key=True)

    # Task name
    title = db.Column(db.String(100), nullable=False)

    # Estimated duration in minutes
    duration = db.Column(db.Integer, nullable=False)

    # Whether the task is completed
    completed = db.Column(db.Boolean, default=False)
