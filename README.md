# Expense Tracker API

A beginner-friendly REST API built with **Python, FastAPI, SQLAlchemy and SQLite** for managing personal expenses.

## Features

- Create, read, update and delete expenses (CRUD)
- Filter expenses by category
- Validate input with Pydantic
- Store data in a relational SQL database
- Category-wise spending summary using SQL aggregation
- Automatic interactive API documentation through FastAPI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app:app --reload
```

Open the interactive documentation:

`http://127.0.0.1:8000/docs`

## Example request

POST `/expenses`

```json
{
  "title": "Groceries",
  "category": "Food",
  "amount": 850,
  "expense_date": "2026-09-01"
}
```

## Interview talking points

- FastAPI is used to expose REST endpoints.
- Pydantic validates incoming request data.
- SQLAlchemy maps the Python `Expense` model to the SQL table.
- CRUD endpoints demonstrate database operations.
- The category summary uses SQL `GROUP BY` and `SUM`.
- The project demonstrates API development, validation, persistence and basic SQL-backed application design.
