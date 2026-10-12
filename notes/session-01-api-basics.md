# Session 1: API Basics

## Core ideas

- An API is a defined way for one software system to communicate with another.
- A REST API is designed around resources and HTTP operations. Our resource is `Customer`.
- HTTP is the communication protocol between a client and the FastAPI server.
- JSON is the common format for exchanging data.
- Client: whatever makes the request (browser, Postman, frontend, another service). Server: whatever receives and processes it. Here, FastAPI is the server.

## HTTP methods

| Method | Endpoint | Meaning |
| --- | --- | --- |
| GET | `/customers` | Get customers |
| GET | `/customers/101` | Get customer 101 |
| POST | `/customers` | Create a customer |
| PUT | `/customers/101` | Update customer 101 |
| DELETE | `/customers/101` | Delete customer 101 |

## Request and response flow

```
Client -> HTTP Request -> FastAPI -> Python logic -> Database -> FastAPI -> JSON Response -> Client
```

An HTTP request can contain a method, URL, headers, parameters and a body.

## Where FastAPI fits

FastAPI is the API/backend framework that exposes functionality through HTTP. It is not the database, the business logic, the LLM, the RAG system or the vector database.

## Mental model

A client sends an HTTP request to an API. FastAPI receives that request through an endpoint, processes it using Python/business logic, may interact with a database or another service, and then sends an HTTP response, usually containing JSON.

## First application

```
pip install fastapi uvicorn
uvicorn main:app --reload
```

- `from fastapi import FastAPI` imports the framework.
- `app = FastAPI()` creates the application.
- `@app.get("/")` creates a GET endpoint at `/`.
- The function below the decorator runs when the endpoint is called.
- The returned dictionary is sent back as the response.

Open `http://127.0.0.1:8000/` for the response and `http://127.0.0.1:8000/docs` for the interactive documentation.

Code: `practice/session_01_first_app.py`
