# -------------------------
# 1️⃣ IMPORTS
# -------------------------

# Flask core functionality
from flask import Flask, render_template, request, redirect

# Database object
from database import db

# Task model
from models import Task


# -------------------------
# 2️⃣ CREATE FLASK APP
# -------------------------

app = Flask(__name__)


# -------------------------
# 3️⃣ APP CONFIGURATION
# -------------------------

# Tell Flask where the SQLite database lives
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

# Disable unnecessary tracking (performance optimization)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# -------------------------
#  INITIALIZE DATABASE
# -------------------------

# Connect SQLAlchemy to this Flask app
db.init_app(app)

# Create database tables if they do not exist
with app.app_context():
    db.create_all()


# =====================================================
#  ROUTES (CRUD OPERATIONS)
# =====================================================

# -------------------------
# READ – Show all tasks
# -------------------------
@app.route("/")
def home():
    # Query all tasks from the database
    tasks = Task.query.all()

    # Send tasks to the HTML template
    return render_template("index.html", tasks=tasks)


# -------------------------
# CREATE – Add a new task
# -------------------------
@app.route("/add", methods=["POST"])
def add_task():
    # Get form data from HTML
    title = request.form["title"]
    duration = request.form["duration"]

    # Create a new Task object
    new_task = Task(
        title=title,
        duration=duration
    )

    # Save task to the database
    db.session.add(new_task)
    db.session.commit()

    # Redirect back to home page
    return redirect("/")


# -------------------------
# DELETE – Remove a task
# -------------------------
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    # Find task by ID or return 404 if not found
    task = Task.query.get_or_404(task_id)

    # Delete task from database
    db.session.delete(task)
    db.session.commit()

    # Redirect back to home page
    return redirect("/")


# -------------------------
# 6️⃣ RUN THE APPLICATION
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
