# Expense Tracker API

A beginner-friendly REST API built with **Python, FastAPI, SQLAlchemy, and SQLite** for managing personal expenses.

## Features

- Create, read, update, and delete expenses (CRUD)
- Filter expenses by category
- Validate request data using Pydantic
- Store expenses in a relational SQL database
- Generate category-wise spending summaries using SQL aggregation
- Interactive API documentation with Swagger UI and ReDoc

## Tech Stack

- **Python** – Programming language
- **FastAPI** – REST API framework
- **SQLAlchemy** – ORM for database operations
- **SQLite** – Relational database
- **Pydantic** – Request and data validation
- **Uvicorn** – ASGI server

## Project Structure

```text
Expense-Tracker-REST-API/
│
├── app.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
└── README.md
