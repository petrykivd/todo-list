# todo-list

This is a simple ToDo list application built with Django. It provides basic functionality for managing tasks and tags.

# Task|Hub Home Page Layout
![image](https://github.com/petrykivd/todo-list/assets/111526221/2e3cc5a6-9cb9-48bc-b258-9bb398ddad60)

## Features

- **Task Management**:
  - View a list of tasks.
  - Create a new task.
  - Update an existing task.
  - Delete a task.
  - Mark a task as done.

- **Tag Management**:
  - View a list of tags.
  - Create a new tag.
  - Update an existing tag.
  - Delete a tag.

## Getting Started

1. Clone the repository: ` git clone https://github.com/petrykivd/todo-list.git `
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
    - If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).
5. Apply database migrations: `python manage.py migrate`
    - `python manage.py loaddata todo_data_db.json` to load the database dump.
7. Run the development server: `python manage.py runserver`

Visit `http://127.0.0.1:8000/` in your web browser to access the Task Manager.

## Usage
1. Explore the dashboard to view tasks.
2. Create new tasks using the "Add task" button.
3. Manage tags
4. Mark tasks as completed or not.

## Contributing

Feel free to contribute to these enhancements, and let's make todo-list even better!
