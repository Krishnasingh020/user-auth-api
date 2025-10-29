# User Authentication API

A complete user authentication system built with Django REST Framework, JWT tokens, and Docker.

## Features
- Custom User Model with Indian phone number validation
- JWT Token Authentication  
- IP address tracking middleware
- Docker with PostgreSQL database
- REST API endpoints

## Setup
```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## API Endpoints

    POST /api/register/ - User registration

    POST /api/login/ - User login

    GET /api/profile/ - User profile

    POST /api/token/refresh/ - Refresh JWT token

## Testing 
```bash
docker-compose exec web python manage.py test
```
