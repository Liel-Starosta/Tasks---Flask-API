
Tasks - Tasks Manager API

This Flask application provides a RESTful API for managing your tasks.

Features:

Create new tasks
Retrieve all tasks
Get a specific task by ID
Update an existing task
Delete a task


Prerequisites:

Python 3.x (https://www.python.org/downloads/)
Flask (https://flask.palletsprojects.com/)
Flask-SQLAlchemy (https://flask-sqlalchemy.palletsprojects.com/) (or a similar database library)


Setup:

Clone this repository.


Create a virtual environment:

cd "/Home/USER/Dekstop/PROJECT/" python3 -m venv myvenv


Activate the virtual environment:

source myvenv/bin/activate

Install dependencies
pip install -r requirements.txt


Running the API:

Start the development server:
flask run (alternatively run tasks_main.py)




The API will be accessible at http://localhost:5000/.

API Endpoints:

GET /Tasks

Retrieves all tasks in JSON format.
Example:
curl -X GET http://localhost:5000/Tasks



GET /Tasks/<task_id>

Retrieves a specific task by its ID in JSON format.
Example:
curl -X GET http://localhost:5000/Tasks/1


POST /Tasks

Creates a new task.  Requires JSON data in the request body with the following fields:

title (string): The title of the task.
description (string): (Optional) A description of the task.
status (string): (Optional) The task's status (e.g., "not-started", "in-progress", "completed").
priority (string): (Optional) The task's priority (e.g., "low", "medium", "high").
Example:

curl -X POST -H "Content-Type: application/json" -d '{"title": "House Maintenance", "description": "Clean Kitchen", "status": "not-started", "priority": "medium"}' http://localhost:5000/Tasks



PUT /Tasks/<task_id>

Updates an existing task. Requires JSON data in the request body with the same fields as the POST request.
Example:

curl -X PUT -H "Content-Type: application/json" -d '{"title": "Eat", "description": "Eat a balanced meal", "status": "completed", "priority": "high"}' http://localhost:5000/Tasks/4


DELETE /Tasks/<task_id>

Deletes a task by its ID.
Example:
curl -X DELETE http://localhost:5000/Tasks/4

Testing:

This project can be tested using tools like Postman or curl commands.





