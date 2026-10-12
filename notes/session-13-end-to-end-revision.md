# Session 13: End-to-End Project Understanding and Final Revision

## Sessions covered

| Session | Topic | Key concept |
| --- | --- | --- |
| 1 | API fundamentals | Client, server, HTTP and JSON |
| 2 | FastAPI basics | Creating the application and endpoints |
| 3 | GET APIs | Path and query parameters |
| 4 | POST APIs | Request body and JSON |
| 5 | Pydantic | Data validation |
| 6 | CRUD | Create, Read, Update, Delete |
| 7 | MySQL integration | SQLAlchemy and database sessions |
| 8 | Request-to-response flow | How a request gets processed |
| 9 | Error handling | HTTP status codes and `HTTPException` |
| 10 | External APIs | Calling other services using HTTPX |
| 11 | Authentication | Tokens, authentication and authorization |
| 12 | Project architecture | Routers, schemas, services and models |
| 13 | End-to-end revision | Connecting all the concepts |

## Complete flow for creating a customer

1. Client or Swagger UI sends `POST /customers` with JSON.
2. FastAPI endpoint receives the request.
3. Pydantic validates the request data.
4. Business logic and SQLAlchemy process the data and run database operations.
5. MySQL stores the customer in the `customers` table.
6. The API returns the customer's details as JSON.

## Code concepts

| Code | Purpose |
| --- | --- |
| `@app.get()` | Defines a GET endpoint |
| `@app.post()` | Defines a POST endpoint |
| `BaseModel` | Defines and validates request and response data |
| `Depends()` | Provides dependencies such as a database session |
| `db.add()` | Adds an object to a database session |
| `db.commit()` | Commits a database transaction |
| `db.query()` | Queries database records |
| `HTTPException` | Returns a controlled HTTP error |
| `httpx.AsyncClient` | Makes asynchronous HTTP requests |
| `HTTPBearer` | Extracts bearer-token credentials |

`db.add()` stages an object in the session. `db.commit()` commits the transaction. They do not do the same thing.

## GenAI and RAG connection

1. FastAPI receives the question.
2. Authentication verifies the user.
3. The backend validates the request.
4. The application retrieves authorized data or documents.
5. An LLM may generate an answer using that context.
6. FastAPI returns the result as JSON.

Retrieval and LLM components are built on top of these backend concepts. FastAPI does not provide them by itself.

## Revision answers

1. Pydantic validates an incoming request body.
2. 404 is returned when a customer does not exist.
3. HTTPX is used to call an external API.
4. Business logic lives primarily in `services/`.
5. Authentication checks identity. Authorization checks permissions.
