# Session 11: Authentication Fundamentals

- Authentication checks who you are.
- Authorization checks what you are allowed to do.

## Flow

1. Client sends a request with an access token.
2. FastAPI checks the token.
3. Valid token: proceed. Missing or invalid token: reject.

## Bearer token

```
Authorization: Bearer your_access_token
```

`HTTPBearer` extracts the bearer token from the request.

## Example

```python
security = HTTPBearer()


@app.get("/protected")
def protected_route(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    if token != "demo-token":
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return {"message": "Access granted"}
```

Run it and use Authorize in `/docs` with `demo-token`.

This is a demonstration only. The token is hardcoded. A real system needs proper token issuance, validation, expiry and secure secret management.

## Summary

| Concept | Meaning |
| --- | --- |
| Authentication | Verifies identity |
| Authorization | Determines permissions |
| Bearer token | Credential sent in the Authorization header |
| 401 Unauthorized | Authentication missing or invalid |
| 403 Forbidden | Caller lacks permission |
| `Depends()` | Provides a dependency such as authentication logic |

Code: `practice/session_11_authentication.py`
