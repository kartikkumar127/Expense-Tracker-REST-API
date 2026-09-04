#Expense Tracker API

A beginner-friendly REST API built with Python, FastAPI, SQLAlchemy, and SQLite for managing personal expenses.

The API supports creating, viewing, updating, deleting, filtering, and summarizing expenses through REST endpoints.
##FEATURES

- Create, read, update, and delete expenses (CRUD)
- Filter expenses by category
- Limit the number of returned expenses
- Validate request data using Pydantic
- Store expense data in SQLite
- Use SQLAlchemy for database operations
- Generate category-wise spending summaries
- Automatic interactive API documentation with FastAPI
- Return appropriate 404 errors when an expense is not found


##TECH STACK

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

The project uses FastAPI, Uvicorn, SQLAlchemy, and Pydantic as its main dependencies.


##PROJECT STRUCTURE

Expense-Tracker-REST-API/
|
|-- app.py
|-- expenses.db
|-- requirements.txt
|-- sample_requests.json
|-- .gitignore
|-- README.md


The application is implemented in app.py. The SQLite database is configured as expenses.db.


##DATABASE MODEL

The API stores expenses in an "expenses" table.

Each expense contains:

- id           : Integer - Unique expense ID
- title        : String  - Expense title
- category     : String  - Expense category
- amount       : Float   - Expense amount
- expense_date : Date    - Date of the expense

The id field is the primary key. The title and category have length restrictions, while the amount must be greater than zero.


##SETUP

1. Clone the repository

git clone https://github.com/kartikkumar127/Expense-Tracker-REST-API.git
cd Expense-Tracker-REST-API


2. Create a virtual environment

python -m venv venv


3. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate


4. Install dependencies

pip install -r requirements.txt


5. Run the API

uvicorn app:app --reload

The API will be available at:

http://127.0.0.1:8000


API DOCUMENTATION

FastAPI automatically generates interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

You can use Swagger UI to send requests and test the API directly from your browser.


##API ENDPOINTS

GET     /                              Check whether the API is running
POST    /expenses                      Create a new expense
GET     /expenses                      Get expenses
GET     /expenses/{expense_id}         Get a specific expense
PUT     /expenses/{expense_id}         Update an expense
DELETE  /expenses/{expense_id}         Delete an expense
GET     /expenses/summary/by-category  Get spending summary by category


1. HEALTH CHECK

GET /

Example response:

{
  "message": "Expense Tracker API is running"
}


2. CREATE AN EXPENSE

POST /expenses

Example request:

{
  "title": "Groceries",
  "category": "Food",
  "amount": 850,
  "expense_date": "2026-09-01"
}

The API validates the request before saving the expense to the database.

The title must contain between 1 and 120 characters, the category between 1 and 50 characters, and the amount must be greater than zero.

Example response:

{
  "title": "Groceries",
  "category": "Food",
  "amount": 850,
  "expense_date": "2026-09-01",
  "id": 1
}


3. GET EXPENSES

GET /expenses

Returns expenses ordered by the most recent expense date.

Example:

GET /expenses

The endpoint supports two optional query parameters.

Filter by category:

GET /expenses?category=Food

Limit results:

GET /expenses?limit=10

You can also combine them:

GET /expenses?category=Food&limit=10

The default limit is 100, with a maximum of 500.


4. GET AN EXPENSE BY ID

GET /expenses/{expense_id}

Example:

GET /expenses/1

If the expense does not exist, the API returns:

{
  "detail": "Expense not found"
}

with a 404 HTTP status code.


5. UPDATE AN EXPENSE

PUT /expenses/{expense_id}

Example:

PUT /expenses/1

Request body:

{
  "amount": 900
}

The update endpoint allows individual fields to be changed without sending the complete expense object.

You can update:

- title
- category
- amount
- expense_date


6. DELETE AN EXPENSE

DELETE /expenses/{expense_id}

Example:

DELETE /expenses/1

Successful response:

{
  "message": "Expense deleted successfully"
}

If the expense does not exist, the API returns a 404 error.


7. CATEGORY-WISE SPENDING SUMMARY

GET /expenses/summary/by-category

Example:

GET /expenses/summary/by-category

Example response:

[
  {
    "category": "Food",
    "total_amount": 2350.0
  },
  {
    "category": "Transport",
    "total_amount": 1500.0
  }
]

The summary uses SQL aggregation with GROUP BY and SUM to calculate total spending for each category. Results are ordered from the highest total spending to the lowest.


##EXAMPLE API WORKFLOW

Create expenses:

POST /expenses

{
  "title": "Groceries",
  "category": "Food",
  "amount": 850,
  "expense_date": "2026-09-01"
}

POST /expenses

{
  "title": "Bus pass",
  "category": "Transport",
  "amount": 500,
  "expense_date": "2026-09-01"
}

Get all expenses:

GET /expenses

Filter by category:

GET /expenses?category=Food

Get a specific expense:

GET /expenses/1

Update an expense:

PUT /expenses/1

{
  "amount": 900
}

View category summary:

GET /expenses/summary/by-category

Delete an expense:

DELETE /expenses/1

These example requests are also included in the project's sample_requests.json file.


##VALIDATION

The API uses Pydantic models to validate incoming data.

For creating an expense:

- title is required and must be 1-120 characters
- category is required and must be 1-50 characters
- amount is required and must be greater than 0
- expense_date is required and must be a valid date

For updating an expense, all fields are optional, allowing individual values to be changed.


##DATABASE

The application uses SQLite for data storage and SQLAlchemy to interact with the database.

The database is automatically initialized when the application starts.


WHAT THIS PROJECT DEMONSTRATES

This project demonstrates practical backend development concepts including:

- REST API development
- FastAPI routing
- CRUD operations
- Request validation with Pydantic
- SQLAlchemy ORM
- SQLite database integration
- Query parameters
- HTTP status codes
- Error handling
- SQL aggregation
- GROUP BY and SUM
- Interactive API documentation


##POINTS

Why FastAPI?

FastAPI is used to build the REST API and provides automatic request validation and interactive API documentation.

Why Pydantic?

Pydantic is used to validate incoming request data before it is processed by the application.

Why SQLAlchemy?

SQLAlchemy provides an ORM layer for interacting with the SQLite database using Python objects and models.

How is validation handled?

Pydantic models define the expected structure and validation rules for incoming expense data.

How does filtering work?

The /expenses endpoint accepts an optional category query parameter. When provided, the database query filters expenses by that category.

How does the spending summary work?

The category summary groups expenses by category and uses SQL SUM to calculate the total amount spent in each category.

How does the update operation work?

The update endpoint accepts optional fields and updates only the fields provided by the client.


##FUTURE IMPROVEMENTS

Possible improvements for future versions include:

- Add automated tests with Pytest
- Add user authentication
- Add pagination
- Add date-range filtering
- Add monthly spending summaries
- Add budget tracking
- Add Docker support
- Add PostgreSQL support
- Add environment-based configuration
- Add a frontend application


##.GITIGNORE

The project excludes the local SQLite database, virtual environments, Python cache files, and environment files from Git.

