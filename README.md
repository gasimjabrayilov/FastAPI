## TodoAppMysql

FastAPI + MySQL todo app with JWT auth and a simple HTML UI. The backend exposes REST endpoints for todos and users, while the frontend uses Jinja templates and a small JS layer to call the API.

## Features
- User registration and login (JWT)
- CRUD for personal todos
- Admin endpoints for global todo access
- Password and phone number update for users
- HTML pages for login/register/todo management

## Tech Stack
- FastAPI, SQLAlchemy, Alembic
- MySQL (pymysql)
- Jinja2 templates + Bootstrap assets

## Project Layout
- `main.py` FastAPI app entry
- `routers/` auth, todos, admin, user routes
- `models.py` SQLAlchemy models
- `database.py` DB config
- `templates/` Jinja pages
- `static/` JS/CSS assets
- `alembic/` migrations

## Setup

1) Create and activate a virtualenv
```bash
python -m venv .venv
.venv\Scripts\activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Create a MySQL database and user
- Default connection string is in `database.py`:
  `mysql+pymysql://root:0000@127.0.0.1:3306/todoapplicationdatabase`
- Update it to match your local credentials.

4) Create tables
This project calls `Base.metadata.create_all(...)` on startup, so tables are created automatically.

Optional: use Alembic (if you prefer migrations)
```bash
alembic upgrade head
```

5) Run the app
```bash
uvicorn main:app --reload
```

Open the UI at:
- `http://127.0.0.1:8000/auth/login-page`
- `http://127.0.0.1:8000/todos/todo-page`

## API Overview

Auth
- `POST /auth` create user
- `POST /auth/token` login (returns JWT)

Todos (requires JWT)
- `GET /todos` list current user's todos
- `GET /todos/todo/{todo_id}` get one
- `POST /todos/todo` create
- `PUT /todos/todo/{todo_id}` update
- `DELETE /todos/todo/{todo_id}` delete

Admin (role = `admin`)
- `GET /admin/todo` list all todos
- `DELETE /admin/todo/{todo_id}` delete any todo

User
- `GET /user/read` current user profile
- `PUT /user/password` change password
- `PUT /user/phone_number/{phone_number}` update phone number

## Notes
- Tokens are stored in a browser cookie named `access_token` by `static/js/base.js`.
- The included `scriptMysql.sql` is an older schema and does not include all fields in `models.py`.

## Tests
```bash
pytest
```
