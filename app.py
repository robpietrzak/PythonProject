# app.py
# This file creates and runs the Flask application

from flask import Flask, request, jsonify
from database import db
from models import Task

# Create the Flask application
app = Flask(__name__)

# Configure the database (SQLite file)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Connect SQLAlchemy to this Flask app
db.init_app(app)

@app.route("/")
def home():
    return "Flask CRUD App is running!"

#CREATE TASKS HERE
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    task = Task(
        title=data["title"],
        duration=data["duration"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201

#READ TASKS HERE
@app.route("/tasks", methods=["GET"])
def get_tasks():
    #Query all tasks from the database
    tasks = Task.query.all()

    #Convert each task to a dictionary so we can return JSON
    tasks_list = []
    for task in tasks:
        tasks_list.append({
            "id": task.id,
            "title": task.title,
            "duration": task.duration,
            "completed": task.completed
         })

    # Return the list of tasks as JSON
    return {"tasks": tasks_list}

# UPDATE TASKS HERE
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    #Get the task by its ID
    task = Task.query.get(task_id)

    #If task is not found, return 404
    if not task:
        return {"message": "Task not found"}, 404

    #Get the JSON data sent by the client
    data = request.json

    #update task fields if they exist in the request
    if "title" in data:
        task.title = data["title"]
    if "duration" in data:
        task.duration = data["duration"]
    if "completed" in data:
        task.completed = data["completed"]

    #Commit changes to the database
    db.session.commit()

    #Return a success message
    return {"message": "Task updated"}

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    #Look up task by ID
    task = Task.query.get(task_id)

    #If the task doesn't exist, return 404
    if not task:
        return {"message": "Task not found"}, 404

    #Delete task from database
    db.session.delete(task)
    db.session.commit()

    #Return success message
    return {"message": "Task deleted"}

if __name__ == "__main__":
    # Create database tables before the app starts
    with app.app_context():
        db.create_all()

    # Start the development server
    app.run(debug=True)
