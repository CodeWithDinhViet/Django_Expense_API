# Django Expense Tracker API

A backend-only Expense Tracker API built with Django REST Framework and JWT Authentication.

This project allows users to manage income and expense transactions, organize them by categories, filter transaction data, and view financial summaries.

## Features

- User registration
- JWT authentication
- Category CRUD
- Transaction CRUD
- Income and expense tracking
- User-based data isolation
- Admin/staff can view all data
- Filter transactions by type, category, date, and month
- Summary API for total income, total expense, and balance
- Validation: category type must match transaction type
- Tested with Postman

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd django_expense_api
```

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

Server will run at:

```text
http://127.0.0.1:8000/
```

## Authentication

Get JWT token:

```http
POST /api/token/
```

Example body:

```json
{
  "username": "admin",
  "password": "admin123456"
}
```

Example response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

Use the access token in protected APIs:

```http
Authorization: Bearer <access_token>
```

Refresh access token:

```http
POST /api/token/refresh/
```

Example body:

```json
{
  "refresh": "your_refresh_token"
}
```

## API Endpoints

### Auth

```http
POST /api/register/
POST /api/token/
POST /api/token/refresh/
```

### Categories

```http
GET    /api/categories/
POST   /api/categories/
GET    /api/categories/{id}/
PATCH  /api/categories/{id}/
DELETE /api/categories/{id}/
```

### Transactions

```http
GET    /api/transactions/
POST   /api/transactions/
GET    /api/transactions/{id}/
PATCH  /api/transactions/{id}/
DELETE /api/transactions/{id}/
```

### Summary

```http
GET /api/transactions/summary/
```

## Filters

Filter transactions by type:

```http
GET /api/transactions/?type=income
GET /api/transactions/?type=expense
```

Filter by category:

```http
GET /api/transactions/?category=1
```

Filter by date:

```http
GET /api/transactions/?date=2026-05-24
```

Filter by month:

```http
GET /api/transactions/?month=5
```

Summary with filter:

```http
GET /api/transactions/summary/?month=5
```

## Example Register

```http
POST /api/register/
```

Body:

```json
{
  "username": "user1",
  "password": "user1123456"
}
```

## Example Create Category

```http
POST /api/categories/
```

Body:

```json
{
  "name": "Food",
  "type": "expense"
}
```

Example response:

```json
{
  "id": 1,
  "user": "user1",
  "name": "Food",
  "type": "expense",
  "created_at": "2026-05-24T10:00:00Z"
}
```

## Example Create Income Transaction

```http
POST /api/transactions/
```

Body:

```json
{
  "category": 2,
  "title": "Monthly Salary",
  "amount": "10000000.00",
  "type": "income",
  "date": "2026-05-24",
  "note": "May salary"
}
```

## Example Create Expense Transaction

```http
POST /api/transactions/
```

Body:

```json
{
  "category": 1,
  "title": "Lunch",
  "amount": "50000.00",
  "type": "expense",
  "date": "2026-05-24",
  "note": "Lunch meal"
}
```

## Example Summary Response

```json
{
  "total_income": 10000000.0,
  "total_expense": 50000.0,
  "balance": 9950000.0
}
```

## Validation Rules

Category type must match transaction type.

For example, if category is:

```json
{
  "name": "Food",
  "type": "expense"
}
```

Then transaction must use:

```json
{
  "type": "expense"
}
```

If transaction type is different, the API returns:

```json
{
  "category": [
    "Category type must match transaction type."
  ]
}
```

## Permissions

- Users must be authenticated to manage categories and transactions.
- Normal users can only view and manage their own data.
- Admin/staff users can view all categories and transactions.
- JWT access token is required for protected endpoints.

## Project Structure

```text
django_expense_api/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── expenses/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Main Concepts Practiced

- Django models
- Model relationships with ForeignKey
- Django migrations
- Django REST Framework serializers
- ModelViewSet
- JWT authentication
- Permission handling
- Query params filtering
- Aggregation with Sum
- API testing with Postman
- Git and GitHub workflow