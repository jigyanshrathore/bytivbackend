# bytivbackend


# Django To-Do List API with JWT Authentication

This project is a RESTful API built using Django and Django REST Framework (. It provides a secure way to manage tasks in a To-Do list with JWT-based authentication. Users can register, log in, and perform CRUD operations on tasks.


## Features
- **User Registration**: Register a new user account.
- **JWT Authentication**: Secure endpoints with access and refresh tokens.
- **Task Management**:
  - Create a task
  - Retrieve all tasks or a specific task by ID
  - Update the status of a task
  - Delete a task
- **Logout**: Revoke tokens using Simple JWT’s blacklist feature.

---

## Prerequisites
- Python 3.8+
- Django 4.x
- Virtual environment (optional but recommended)

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   
```

### 3. Install Dependencies
```bash
pip install dependecies // mentioned at the end
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### 6. Run the Development Server
```bash
python manage.py runserver
```

---

## API Endpoints

### Authentication
| Method | Endpoint              | Description                     |
|--------|------------------------|---------------------------------|
| POST   | `/tasks/register/`     | Register a new user             |
| POST   | `/api/token/`          | Obtain JWT access and refresh tokens |
| POST   | `/api/token/refresh/`  | Refresh an expired access token |
| POST   | `/api/token/verify/`   | Verify the validity of a token  |
| POST   | `/api/logout/`         | Revoke refresh token (logout)   |

### Task Management
| Method | Endpoint              | Description                     |
|--------|------------------------|---------------------------------|
| GET    | `/tasks/`              | Fetch all tasks                 |
| POST   | `/tasks/create/`       | Create a new task               |
| GET    | `/tasks/<id>/`         | Retrieve a specific task by ID  |
| PUT    | `/tasks/<id>/update/`  | Update a task's status          |
| DELETE | `/tasks/<id>/delete/`  | Delete a task by ID             |

---

## Example Requests

### 1. Register a User
**Endpoint**: `POST /tasks/register/`  
**Request Body**:
```json
{
    "username": "jigyasnh",
    "password": "securepassword123"
}
```
**Response**:
```json
{
    "message": "User registered successfully"
}
```

---

### 2. Obtain Tokens
**Endpoint**: `POST /api/token/`  
**Request Body**:
```json
{
    "username": "jigyansh",
    "password": "securepassword123"
}
```
**Response**:
```json
{
    "access": "access_token_here",
    "refresh": "refresh_token_here"
}
```

---

### 3. Create a Task
**Endpoint**: `POST /tasks/create/`  
**Headers**:
```
Authorization: Bearer <access_token>
```
**Request Body**:
```json
{
    "title": "Buy Groceries",
    "description": "blah, Eggs, Bread"
}
```
**Response**:
```json
{
    "id": 1,
    "title": "Buy Groceries",
    "description": "blah, Eggs, Bread",
    "status": "pending"
}
```

---

### 4. Refresh Access Token
**Endpoint**: `POST /api/token/refresh/`  
**Request Body**:
```json
{
    "refresh": "refresh_token_here"
}
```
**Response**:
```json
{
    "access": "new_access_token_here"
}
```

---

### 5. Logout
**Endpoint**: `POST /api/logout/`  
**Request Body**:
```json
{
    "refresh": "refresh_token_here"
}
```
**Response**:
```json
{
    "message": "Successfully logged out"
}
```



Key dependencies:
- Django: Web framework for building the application.
- Django REST Framework: For creating RESTful APIs.
- Simple JWT: For JWT-based authentication.

