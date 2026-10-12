# Session 12: Real Project Structure

A larger FastAPI project separates responsibilities into different files and folders. This is a common style, not a mandatory structure.

```
customer_management_api/
    main.py
    routers/
    schemas/
    models/
    services/
    database/
    requirements.txt
    .env
```

| Layer | Responsibility | Example |
| --- | --- | --- |
| Router | Receives API requests | `POST /customers` |
| Schema | Validates input and defines response shape | Customer name, age, city |
| Service | Applies business rules | Check whether a customer can be updated |
| Model | Represents database data | `customers` table |
| Database | Stores and retrieves records | MySQL |

## Flow

```
main.py -> routers/customers.py -> schemas/customer.py -> services/customer_service.py -> models + database -> JSON response
```

- `requirements.txt` lists dependencies.
- `.env` holds local configuration and secrets and is excluded from GitHub.

In a small project some of these responsibilities can stay in the same file. This repository keeps the simple Session 7 layout: `main.py`, `database.py` and `models.py`.
