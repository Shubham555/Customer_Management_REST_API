# Session 7: MySQL, SQLAlchemy and Database Integration

## Roles

| Component | Job |
| --- | --- |
| FastAPI | Receives HTTP requests and returns responses |
| Pydantic | Validates incoming request data |
| SQLAlchemy | Lets Python work with MySQL |
| MySQL | Stores records permanently |

## Setup

```sql
CREATE DATABASE customer_management;
```

```
pip install fastapi uvicorn sqlalchemy pymysql
```

The `customers` table is created by SQLAlchemy from the Python model.

## Files

- `database.py`: connection URL, `create_engine`, `SessionLocal`, `Base`.
- `models.py`: `CustomerDB`, the SQLAlchemy model for the `customers` table.
- `main.py`: Pydantic models, session dependency and endpoints.

## database.py

- `DATABASE_URL` says which database to connect to and which driver to use.
- `create_engine()` creates the engine that manages connections.
- `SessionLocal` creates database sessions.
- `Base` is the foundation for table classes.

## Two models

- `Customer` (Pydantic): validates data coming into the API.
- `CustomerDB` (SQLAlchemy): represents rows in MySQL.
- `CustomerResponse` adds `id` and uses `from_attributes=True` so database objects can be returned.

## Key calls

- `Depends(get_db)`: provides a database session to the endpoint.
- `db.add()`: stages a new record.
- `db.commit()`: commits the transaction.
- `db.refresh()`: reloads the record so generated values such as `id` are available.
- `db.query(...).filter(...).first()`: finds a matching record.
- `db.delete()`: marks a record for deletion. `commit()` makes it permanent.
- `response_model`: defines the shape of the response.
- `try/finally` in `get_db()` closes the session after each request, even on error.

## Flow

```
HTTP request -> FastAPI endpoint -> Pydantic validation -> SQLAlchemy -> MySQL -> JSON response
```

## Notes

- If the MySQL password contains URL-special characters such as `@` or `/`, the URL needs proper encoding.
- Keep real credentials out of source control.

Code: `main.py`, `database.py`, `models.py`
