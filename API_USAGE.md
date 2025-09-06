# API Usage Guide

## Authentication

The API uses Token-based authentication. You need to obtain a token first and then use it in subsequent requests.

### 1. Login to get a token

```bash
curl --location 'localhost:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "a",
    "password": "a"
}'
```

**Response:**
```json
{
    "token": "0b9ae99acf81e9881f2c5bce55ad531d3ae6eb0b",
    "user_id": 1,
    "username": "a",
    "email": "a@a.com",
    "message": "Login successful"
}
```

### 2. Use the token for authenticated requests

Include the token in the `Authorization` header:

```bash
curl --location 'localhost:8000/api/auth/user/' \
--header 'Authorization: Token YOUR_TOKEN_HERE'
```

### 3. Available Authentication Endpoints

- **POST** `/api/auth/login/` - Login and get token
- **POST** `/api/auth/logout/` - Logout and delete token (requires authentication)
- **GET** `/api/auth/user/` - Get current user info (requires authentication)

## API Endpoints

### Products API

```bash
# List all product endpoints
curl --location 'localhost:8000/products/' \
--header 'Authorization: Token YOUR_TOKEN_HERE'

# Get products
curl --location 'localhost:8000/products/products/' \
--header 'Authorization: Token YOUR_TOKEN_HERE'

# Get categories  
curl --location 'localhost:8000/products/categories/' \
--header 'Authorization: Token YOUR_TOKEN_HERE'
```

## Example Workflow

1. **Login:**
```bash
TOKEN=$(curl -s --location 'localhost:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data '{"username": "a", "password": "a"}' | jq -r '.token')
```

2. **Use the token:**
```bash
curl --location 'localhost:8000/products/products/' \
--header "Authorization: Token $TOKEN"
```

3. **Logout:**
```bash
curl --location 'localhost:8000/api/auth/logout/' \
--header "Authorization: Token $TOKEN" \
--request POST
```

## Admin Interface

You can also use the Django admin interface:
- **URL**: http://localhost:8000/admin/
- **Username**: a
- **Password**: a

## Browsable API

Django REST Framework provides a browsable API interface:
- **URL**: http://localhost:8000/api/
- Login using the session authentication for web browsing

