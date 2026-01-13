# To-Do List CRUD Application

## Overview

This project is a **full-stack Python Flask CRUD (Create, Read, Update, Delete) application** that allows users to manage a daily to-do list through a **web browser interface**.

Users can create, view, update, and delete tasks using HTML forms, while Flask handles backend logic and database persistence using SQLite and SQLAlchemy.

This project was built as a **portfolio project** to demonstrate full-stack fundamentals, REST concepts, and clean backend/frontend integration.

---

## Features

* Add tasks using a browser-based form
* View all tasks in a list
* Edit/update existing tasks
* Delete tasks
* Persistent storage using SQLite
* Simple and intuitive HTML interface

---

## Technologies Used

* **Python 3**
* **Flask** – Backend web framework
* **Flask-SQLAlchemy** – ORM for database management
* **SQLite** – Relational database
* **HTML & Jinja2** – Frontend templating
* **Git & GitHub** – Version control

---

## Project Structure

```
todo-crud-app/
│
├── app.py              # Flask application and routes
├── models.py           # Database models
├── database.py         # Database initialization
├── templates/          # HTML templates
│   ├── index.html      # Main task list page
│   └── edit.html       # Edit task page
├── instance/
│   └── tasks.db        # SQLite database (auto-generated)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How It Works

### Frontend (HTML)

The frontend uses HTML forms and Jinja2 templates to allow users to interact with the application through a browser. User actions such as adding, editing, or deleting tasks send HTTP requests to Flask routes.

### Backend (Flask)

Flask receives requests from the frontend, processes the data, and interacts with the database using SQLAlchemy.

### Database

Each task includes:

* `id` – Unique identifier
* `title` – Task description
* `duration` – Estimated time to complete (minutes)

The database is automatically created when the application starts.

---

## Routes and Functionality

| Action      | Route          | Method |
| ----------- | -------------- | ------ |
| View tasks  | `/`            | GET    |
| Add task    | `/add`         | POST   |
| Edit task   | `/edit/<id>`   | GET    |
| Update task | `/update/<id>` | POST   |
| Delete task | `/delete/<id>` | POST   |

---

## Running the Application

### 1. Clone the Repository

```bash
git clone https://github.com/robpietrzak/PythonProject.git
cd PythonProject
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\\Scripts\\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Future Improvements

* Task completion status (checkbox)
* Daily start and end time tracking
* CSS styling for improved UI
* User authentication
* Deployment to a cloud platform

---

## Author

**Robert Pietrzak**
Entry-Level Software Engineer / Game Developer

---

## License

This project is for educational and portfolio purposes.
