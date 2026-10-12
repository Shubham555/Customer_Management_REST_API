# Customer Management REST API

A beginner-friendly FastAPI project for managing customer records with MySQL and SQLAlchemy.

## Features
- Create, list, retrieve, update, and delete customers
- Pydantic request validation
- `404 Not Found` responses for missing customers
- Interactive Swagger UI documentation

> **Project status:** Initial implementation package. Configure your local MySQL connection and run the verification steps before describing it as fully tested.

## Technology stack
- Python
- FastAPI and Uvicorn
- SQLAlchemy
- MySQL and PyMySQL
- Pydantic

## Project structure

```text
customer_management_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── customer.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── customer.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── customers.py
│   └── services/
│       ├── __init__.py
│       └── customer_service.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 1. Prerequisites
Install Python 3.10 or newer and MySQL Server. MySQL Workbench can be used to run SQL statements.

## 2. Create the MySQL database
Run this in MySQL Workbench:

```sql
CREATE DATABASE customer_management;
```

The application creates the `customers` table automatically at startup if it does not already exist.

## 3. Configure environment variables
Copy `.env.example` to a new file named `.env`, then replace the placeholders with your own MySQL credentials.

```env
DATABASE_URL=mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost:3306/customer_management
```

Never commit `.env` or real passwords to GitHub. If your password contains URL-reserved characters, URL-encode them or configure the SQLAlchemy URL with a URL object.

## 4. Create and activate a virtual environment

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 5. Install dependencies
```bash
python -m pip install -r requirements.txt
```

## 6. Start the API
Run from the project root:

```bash
uvicorn app.main:app --reload
```

Open:
- API home: http://127.0.0.1:8000/
- Interactive documentation: http://127.0.0.1:8000/docs

## 7. Test the API
Use Swagger UI at `/docs`.

### Create a customer
`POST /customers`
```json
{
  "name": "Rahul",
  "age": 25,
  "city": "Pune"
}
```

### Available endpoints
- `GET /customers` — list customers
- `GET /customers/{customer_id}` — retrieve one customer
- `PUT /customers/{customer_id}` — replace editable customer fields
- `DELETE /customers/{customer_id}` — delete a customer

A missing customer returns `404 Not Found`. Invalid request data is validated by FastAPI/Pydantic.

## Database table
The app creates one `customers` table:

| Column | Type | Purpose |
|---|---|---|
| `id` | Integer, primary key | Unique customer ID |
| `name` | String(100), required | Customer name |
| `age` | Integer, required | Customer age |
| `city` | String(100), required | Customer city |

## Notes
- This is a learning project and should be reviewed and tested before production use.
- Authentication, authorization, database migrations, automated tests, and production deployment are not included in this initial version.
- The authentication and external API examples from the learning sessions were separate practice examples and are not enabled in this customer CRUD API.
