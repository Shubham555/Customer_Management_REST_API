# Session 9: Error Handling and HTTP Status Codes

## Status codes

| Code | Meaning | Example |
| --- | --- | --- |
| 200 | OK | Customer retrieved |
| 201 | Created | New customer created |
| 204 | No Content | Success with no body |
| 400 | Bad Request | Invalid request |
| 401 | Unauthorized | Authentication required or invalid |
| 403 | Forbidden | No permission |
| 404 | Not Found | Customer ID does not exist |
| 422 | Validation Error | Request data fails validation |
| 500 | Internal Server Error | Unexpected server failure |

Focus first on 200, 201, 404, 422 and 500.

## HTTPException

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Customer not found"
)
```

- `status_code` tells the client what kind of error occurred.
- `detail` is the message.
- `raise` stops normal execution of the endpoint.

## In the project

When SQLAlchemy finds no matching customer, the GET one, PUT and DELETE endpoints return `404`.

## Unexpected errors

A `500` can occur if MySQL is unavailable or there is a bug. Log technical details for debugging and return a safe message. Do not expose passwords, stack traces or sensitive information.

Code: `practice/session_09_error_handling.py`
