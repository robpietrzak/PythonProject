# To-Do List CRUD Application

## Overview
This project is a **Python Flask CRUD (Create, Read, Update, Delete) application** that serves as a backend API for a To-Do list. It allows users to create tasks, view all tasks, update existing tasks, and delete tasks. The application uses **Flask** for the web framework and **SQLite with SQLAlchemy** for data persistence.

This project was built as a **portfolio project** to demonstrate backend development fundamentals, RESTful API design, and database integration.

---

## Features

- Create new tasks with a title and estimated duration
- View all existing tasks
- Update task details (title, duration, completion status)
- Delete tasks by ID
- Persistent storage using SQLite
- RESTful API endpoints

---

## Technologies Used

- **Python 3**
- **Flask** – Web framework
- **Flask-SQLAlchemy** – ORM for database interactions
- **SQLite** – Lightweight relational database
- **Git & GitHub** – Version control
- **Postman** – API testing

---

## Project Structure

```
todo-crud-app/
│
├── app.py          # Main Flask application and routes
├── models.py       # Database models
├── database.py     # Database initialization
├── instance/
│   └── tasks.db    # SQLite database (generated at runtime)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How It Works

### Database
The application uses SQLite as its database. When the application starts, SQLAlchemy automatically creates the database and tables if they do not already exist.

Each task contains:
- `id` – Unique identifier
- `title` – Task name
- `duration` – Estimated time to complete (in minutes)
- `completed` – Boolean indicating completion status

---

## API Endpoints

### Create a Task
**POST** `/tasks`

Request Body (JSON):
```json
{
  "title": "Build CRUD app",
  "duration": 60
}
```

Response:
```json
{
  "message": "Task created"
}
```

---

### Read All Tasks
**GET** `/tasks`

Response:
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Build CRUD app",
      "duration": 60,
      "completed": false
    }
  ]
}
```

---

### Update a Task
**PUT** `/tasks/<id>`

Request Body (JSON):
```json
{
  "title": "Updated task title",
  "completed": true
}
```

Response:
```json
{
  "message": "Task updated"
}
```

---

### Delete a Task
**DELETE** `/tasks/<id>`

Response:
```json
{
  "message": "Task deleted"
}
```

---

## Running the Application

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/todo-crud-app.git
cd todo-crud-app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
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

The server will start at:
```
http://127.0.0.1:5000
```

---

## Testing the API

This application is designed to be tested using **Postman** or similar API tools.

You can also test the read endpoint directly in a browser:
```
http://127.0.0.1:5000/tasks
```

---

## Future Improvements

- Add user authentication
- Add daily start/end time tracking
- Frontend UI using React or HTML/CSS
- Pagination and filtering
- Deployment to a cloud service (Render, Fly.io, or AWS)

---

## Author

**Robert Pietrzak**  
Entry-Level Software Engineer / Game Developer

---

## License

This project is for educational and portfolio purposes.

