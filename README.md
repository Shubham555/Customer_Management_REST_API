# Customer Management API

A FastAPI project built from my FastAPI learning. It performs real CRUD operations on a MySQL database, with business rules, filtering, sorting and paging, validation, error handling, an external API import and bearer-token authentication.

## Project structure

```
customer-management-api/
├── main.py
├── auth.py
├── requirements.txt
├── README.md
├── .gitignore
├── database/
│   └── connection.py
├── models/
│   └── customer.py
├── schemas/
│   └── customer.py
├── services/
│   └── customer_service.py
└── routers/
    ├── customers.py
    └── external.py
```

## Request flow

```
Client -> main.py -> router -> auth and Pydantic validation -> service rules -> SQLAlchemy model -> MySQL -> JSON response
```

## Business rules

- Age must be between 18 and 100, otherwise 400.
- Email must be unique, otherwise 400.
- sort_by must be id, name or age, order must be asc or desc, limit must be 1 to 100, skip must be 0 or more, otherwise 400.
- A customer that does not exist returns 404.
- Invalid data types or missing fields return 422.

## Setup (Windows, VS Code)

1. Extract the zip and open the folder in VS Code (File, Open Folder).
2. Open the terminal and create the virtual environment:

```
python -m venv .venv
```

3. Activate it. In PowerShell:

```
.venv\Scripts\Activate.ps1
```

In Command Prompt:

```
.venv\Scripts\activate
```

If PowerShell blocks the script, run this once and activate again:

```
Set-ExecutionPolicy -Scope Process Bypass
```

4. Select the interpreter: Ctrl + Shift + P, then "Python: Select Interpreter", then choose the one with `.venv`.
5. Install the packages:

```
pip install -r requirements.txt
```

6. In MySQL Workbench, create the database:

```sql
CREATE DATABASE customer_management;
```

If you already created a `customers` table with an older version of this project, drop it first so the new columns are created:

```sql
DROP TABLE IF EXISTS customer_management.customers;
```

7. Set the credentials and the API token in the same terminal (PowerShell):

```
$env:DB_USER="root"
$env:DB_PASSWORD="your_mysql_password"
$env:API_TOKEN="choose_any_token"
```

In Command Prompt use `set DB_USER=root`, `set DB_PASSWORD=your_mysql_password` and `set API_TOKEN=choose_any_token`.

8. Run the app:

```
uvicorn main:app --reload
```

The app will not start if `API_TOKEN` is not set.

9. Check the connection in MySQL Workbench:

```sql
USE customer_management;
SHOW TABLES;
DESCRIBE customers;
```

The `customers` table is created automatically when the app starts. If you see it with `id`, `name`, `email`, `age` and `city`, the MySQL connection is working.

The environment variables last only for that terminal window. Set them again in any new terminal.

## Endpoints

| Method | Endpoint | Description | Token needed |
| --- | --- | --- | --- |
| GET | `/` | Health check | No |
| POST | `/customers` | Create a customer, returns 201 | Yes |
| GET | `/customers` | List customers with filters, sorting and paging | No |
| GET | `/customers/{customer_id}` | Get one customer | No |
| PUT | `/customers/{customer_id}` | Update a customer | Yes |
| DELETE | `/customers/{customer_id}` | Delete a customer, returns 204 | Yes |
| GET | `/external-user/{user_id}` | Fetch a user from jsonplaceholder | No |
| POST | `/customers/import/{user_id}?age=30` | Fetch a jsonplaceholder user and save it as a customer, returns 201 | Yes |

`GET /customers` query parameters: `city`, `name` (search), `sort_by` (id, name, age), `order` (asc, desc), `skip`, `limit`.

## Authentication

Create, update, delete and import need a bearer token. It is the value of the `API_TOKEN` environment variable. In `http://127.0.0.1:8000/docs`, click Authorize and enter the same value. This is a simple token check for learning, not production authentication.

## Test checklist

Open `http://127.0.0.1:8000/docs`, click Authorize and enter your token. After each database operation, check MySQL Workbench with `SELECT * FROM customers;`.

| # | Test | Expected |
| --- | --- | --- |
| 1 | `GET /` | `{"message": "API is working"}` |
| 2 | `POST /customers` with `{"name": "Rahul", "email": "rahul@example.com", "age": 25, "city": "Pune"}` | 201, customer with an id, new row in MySQL |
| 3 | `POST /customers` with `{"name": "Amit", "email": "amit@example.com", "age": 27, "city": "Mumbai"}` | 201 |
| 4 | `POST /customers` with `{"name": "Priya", "email": "priya@example.com", "age": 31, "city": "Pune"}` | 201 |
| 5 | `GET /customers` | All three customers |
| 6 | `GET /customers?city=Pune` | Rahul and Priya |
| 7 | `GET /customers?name=ri` | Priya |
| 8 | `GET /customers?sort_by=age&order=desc` | Priya, Amit, Rahul |
| 9 | `GET /customers?skip=1&limit=1` | One customer, the second in the list |
| 10 | `GET /customers/1` | Rahul |
| 11 | `PUT /customers/1` with `{"name": "Rahul", "email": "rahul@example.com", "age": 26, "city": "Pune"}` | Age updated, row updated in MySQL |
| 12 | `DELETE /customers/2` | 204, row gone in MySQL |
| 13 | `GET /customers/999` | 404 "Customer not found" |
| 14 | `POST /customers` with `rahul@example.com` again | 400 "Email already exists" |
| 15 | `POST /customers` with age 10 | 400 age error |
| 16 | `POST /customers` with age "banana" | 422 validation error |
| 17 | `POST /customers` with the `name` field missing | 422 validation error |
| 18 | `GET /customers?sort_by=salary` | 400 sort_by error |
| 19 | `GET /customers?limit=500` | 400 limit error |
| 20 | `PUT /customers/999` | 404 |
| 21 | `POST /customers` without the token | 401 or 403, no row added |
| 22 | `POST /customers` with a wrong token | 401 "Invalid token" |
| 23 | `GET /external-user/1` | User JSON from jsonplaceholder (needs internet) |
| 24 | `POST /customers/import/1?age=30` | 201, a new customer from the external user, row in MySQL |
| 25 | `POST /customers/import/1?age=30` again | 400 "Email already exists" |
| 26 | `POST /customers/import/999?age=30` | 502 "External service request failed" |

## Common errors

| Error | Cause |
| --- | --- |
| `API_TOKEN environment variable is not set` | Set `API_TOKEN` in the terminal before running |
| `Access denied for user` | Wrong MySQL username or password |
| `Can't connect to MySQL server` | MySQL service is not running |
| `Unknown database 'customer_management'` | The database was not created in step 6 |
| `Unknown column 'email'` | An older `customers` table exists, drop it as in step 6 |
| `No module named pymysql` | Packages not installed in the active `.venv` |
| `No module named database` | uvicorn was not started from the project folder |
