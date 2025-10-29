# User Authentication API - NEXTBIGE Challenge 1

A complete user authentication system built with Django REST Framework, JWT tokens, and Docker as per NEXTBIGE Challenge 1 requirements.

## 📋 Assignment Requirements Met

- ✅ Custom User Model extending Django's AbstractUser
- ✅ Indian phone number validation
- ✅ JWT token authentication
- ✅ Custom middleware for IP address capture
- ✅ REST API endpoints (register, login, profile)
- ✅ Docker and Docker Compose with PostgreSQL
- ✅ Pytest test cases
- ✅ Class-based views
- ✅ Proper project structure and documentation

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose

### Installation & Setup

1. **Clone or extract the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd user-auth-api
   
   # If using zip file, extract and navigate to the directory
   '''


2. Build and start the containers
```bash
docker-compose up --build
```
This will:

    Build the Django application container

    Start PostgreSQL database container

    Run the application on http://localhost:8000

3. Apply database migrations (in a new terminal)
```bash
docker-compose exec web python manage.py migrate
```
4. Create a superuser (optional, for admin access)
```bash
docker-compose exec web python manage.py createsuperuser
```
5. Run tests to verify everything works
```bash
docker-compose exec web python manage.py test
```

## Project Structure
```bash
user-auth-api/
├── Dockerfile                 # Docker container configuration
├── docker-compose.yml         # Multi-container setup
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management script
├── .dockerignore             # Docker ignore rules
├── .gitignore                # Git ignore rules
├── README.md                 # This file
├── core/                     # Django project
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py
│   └── middleware.py         # Custom IP capture middleware
└── users/                    # Custom user app
    ├── __init__.py
    ├── admin.py              # Admin panel configuration
    ├── apps.py
    ├── models.py             # CustomUser model
    ├── serializers.py        # DRF serializers
    ├── tests.py              # Unit tests
    ├── urls.py               # API URL routes
    └── views.py              # API views
```

## Api Endpoints 

1. User Registration 
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepass123",
    "phone_number": "+919876543210",
    "date_of_birth": "1990-01-01"
  }'
```

2. User Login 
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "securepass123"
  }'

```

3. User Profile
```bash
curl -X GET http://localhost:8000/api/profile/ \
  -H "Authorization: Bearer <your_access_token>"
```

4. Token Refresh 
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "<your_refresh_token>"
  }'
```

## testing 
```bash
docker-compose exec web python manage.py test
```

Test Coverage

The test suite includes:

    User model creation tests

    API endpoint tests (registration, login, profile)

    Authentication and authorization tests

    Validation tests for Indian phone numbers

## features
    Custom User Model with Indian phone validation

    JWT Authentication

    IP address tracking middleware

    PostgreSQL database in Docker

    REST API endpoints

## Author 
By Krishna-singh
email- [workforkrishnasingh@gmail.com]