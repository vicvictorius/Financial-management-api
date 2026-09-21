# Financial Management API

A RESTful API for personal financial management, built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

The project was developed with a focus on clean architecture, secure authentication, automated testing, containerization, CI/CD, database migrations, and application observability.

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?logo=githubactions)](https://github.com/features/actions)
[![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?logo=prometheus)](https://prometheus.io/)

---

## Overview

**Financial Management API** is a backend application designed to provide a structured and secure way to manage personal financial data.

The API allows authenticated users to create and manage financial transactions, organize them into categories, and visualize financial summaries through dashboard endpoints.

The project also implements a complete development and deployment workflow, including:

* Automated testing
* Code quality checks
* Security analysis
* Docker containerization
* Database migrations
* GitHub Actions CI/CD
* GitHub Container Registry
* Automated deployment to Render
* Prometheus-compatible application metrics

---

## Features

### Authentication

* User registration
* User login
* JWT-based authentication
* Password hashing
* OAuth2 password flow
* Protected endpoints
* User-level data isolation

### Financial Management

* Create financial transactions
* List transactions
* Retrieve individual transactions
* Update transactions
* Delete transactions
* Income and expense management
* Transaction ownership based on authenticated users

### Categories

* Create categories
* List categories
* Retrieve categories by ID
* Duplicate category validation

### Dashboard

* Total income
* Total expenses
* Current balance
* Monthly financial summaries

### Infrastructure & DevOps

* Docker support
* Docker Compose
* PostgreSQL
* Alembic migrations
* GitHub Actions
* GitHub Container Registry
* Automated Render deployment

### Quality & Security

* Pytest integration tests
* Ruff linting
* Bandit security analysis
* pip-audit dependency auditing

### Observability

* Health check endpoint
* Prometheus metrics
* HTTP request counters
* HTTP response duration histograms
* Python process metrics

---

# Architecture

The application follows a layered architecture that separates HTTP routing, business logic, data validation, authentication, and persistence.

```mermaid
flowchart TD
    Client[Client / Frontend]
    API[FastAPI Application]

    Routers[API Routers]
    Services[Service Layer]
    Schemas[Pydantic Schemas]
    Auth[JWT Authentication]
    Models[SQLAlchemy Models]
    DB[(PostgreSQL)]

    Client --> API
    API --> Routers
    Routers --> Services
    Routers --> Schemas
    Routers --> Auth
    Services --> Models
    Models --> DB
```

### Main application layers

| Layer      | Responsibility                      |
| ---------- | ----------------------------------- |
| `routers`  | HTTP endpoints and request handling |
| `services` | Business logic                      |
| `schemas`  | Request/response validation         |
| `models`   | Database entities                   |
| `auth`     | Authentication and authorization    |
| `core`     | Configuration, security and metrics |
| `database` | Database connection and persistence |

This structure keeps responsibilities separated and makes the application easier to maintain and extend.

---

# Tech Stack

## Backend

* **Python 3.14**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **SQLAlchemy**
* **PostgreSQL**

## Authentication & Security

* **JWT**
* **python-jose**
* **Passlib**
* **bcrypt**
* **OAuth2 Password Flow**

## Database & Migrations

* **PostgreSQL**
* **SQLAlchemy**
* **Alembic**

## Testing

* **Pytest**
* **pytest-asyncio**
* **HTTPX**

## Code Quality & Security

* **Ruff**
* **Bandit**
* **pip-audit**

## DevOps

* **Docker**
* **Docker Compose**
* **GitHub Actions**
* **GitHub Container Registry**
* **Render**

## Observability

* **Prometheus**
* **prometheus-client**

---

# Project Structure

```text
financial-management-api/
│
├── app/
│   ├── api/
│   │   └── routers/
│   │       ├── auth.py
│   │       ├── categories.py
│   │       ├── dashboard.py
│   │       ├── health.py
│   │       ├── transactions.py
│   │       └── users.py
│   │
│   ├── auth/
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── metrics.py
│   │   └── security.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── models/
│   │       ├── category.py
│   │       ├── transaction.py
│   │       └── user.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── category.py
│   │   ├── dashboard.py
│   │   ├── token.py
│   │   ├── transaction.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── category_service.py
│   │   ├── dashboard_service.py
│   │   ├── transaction_service.py
│   │   └── user_service.py
│   │
│   └── main.py
│
├── alembic/
│   ├── env.py
│   └── versions/
│
├── tests/
│   ├── integration/
│   │   ├── test_auth.py
│   │   ├── test_categories.py
│   │   ├── test_dashboard.py
│   │   ├── test_health.py
│   │   ├── test_transactions.py
│   │   └── test_users.py
│   └── conftest.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── alembic.ini
├── requirements.txt
├── pytest.ini
├── pyproject.toml
├── SECURITY.md
└── README.md
```

---

# Authentication

The API uses **JWT access tokens** to protect user-specific resources.

Authentication flow:

```mermaid
sequenceDiagram
    Client->>API: POST /auth/register
    API->>Database: Create user
    Database-->>API: User created
    API-->>Client: User response

    Client->>API: POST /auth/login
    API->>Database: Validate credentials
    Database-->>API: User
    API-->>Client: JWT access token

    Client->>API: Protected request + Bearer token
    API->>API: Validate JWT
    API-->>Client: Protected resource
```

Protected requests use:

```http
Authorization: Bearer <access_token>
```

Transaction and dashboard resources are associated with the authenticated user's ID, preventing users from accessing other users' financial records through the normal application flow.

---

# API Endpoints

## Authentication

| Method | Endpoint         | Description                      | Auth |
| ------ | ---------------- | -------------------------------- | ---- |
| `POST` | `/auth/register` | Register a new user              | No   |
| `POST` | `/auth/login`    | Authenticate user and obtain JWT | No   |

### Register

```http
POST /auth/register
```

Example request:

```json
{
  "username": "victor",
  "email": "victor@example.com",
  "password": "password123"
}
```

### Login

```http
POST /auth/login
```

The login endpoint uses `application/x-www-form-urlencoded` data.

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=victor&password=password123"
```

Example response:

```json
{
  "access_token": "your-jwt-token",
  "token_type": "bearer"
}
```

---

## Categories

| Method | Endpoint                    | Description        | Auth |
| ------ | --------------------------- | ------------------ | ---- |
| `POST` | `/categories/`              | Create a category  | No   |
| `GET`  | `/categories/`              | List categories    | No   |
| `GET`  | `/categories/{category_id}` | Get category by ID | No   |

### Create category

```http
POST /categories/
```

Example:

```json
{
  "name": "Food"
}
```

---

## Transactions

All transaction endpoints require JWT authentication.

| Method   | Endpoint                         | Description              | Auth |
| -------- | -------------------------------- | ------------------------ | ---- |
| `POST`   | `/transactions/`                 | Create transaction       | JWT  |
| `GET`    | `/transactions/`                 | List user's transactions | JWT  |
| `GET`    | `/transactions/{transaction_id}` | Get transaction          | JWT  |
| `PUT`    | `/transactions/{transaction_id}` | Update transaction       | JWT  |
| `DELETE` | `/transactions/{transaction_id}` | Delete transaction       | JWT  |

Example authorization header:

```http
Authorization: Bearer <access_token>
```

The API associates each transaction with the authenticated user.

---

## Dashboard

| Method | Endpoint             | Description            | Auth |
| ------ | -------------------- | ---------------------- | ---- |
| `GET`  | `/dashboard/summary` | Financial summary      | JWT  |
| `GET`  | `/dashboard/monthly` | Monthly financial data | JWT  |

Example summary response:

```json
{
  "total_income": 5000,
  "total_expenses": 1850,
  "balance": 3150
}
```

---

## Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

The endpoint is used to verify application availability.

---

# Observability

The application exposes metrics compatible with **Prometheus**.

```http
GET /metrics/
```

Example:

```bash
curl http://localhost:8000/metrics/
```

The application exposes metrics such as:

```text
http_requests_total
http_request_duration_seconds
python_gc_objects_collected_total
process_virtual_memory_bytes
process_resident_memory_bytes
process_cpu_seconds_total
```

### HTTP request metrics

The custom application metrics track:

* HTTP method
* HTTP status code
* Total request count
* Request duration

Example:

```text
http_requests_total{method="GET",status_code="200"} 23.0
```

Request duration is exposed as a Prometheus histogram:

```text
http_request_duration_seconds
```

This allows the application to be integrated with monitoring systems such as Prometheus and Grafana.

---

# Database & Migrations

The application uses **PostgreSQL** as its relational database.

SQLAlchemy is responsible for database interaction, while **Alembic** manages schema migrations.

```text
Application
     │
     ▼
SQLAlchemy
     │
     ▼
PostgreSQL
```

Database migrations can be applied with:

```bash
alembic upgrade head
```

In the production container, migrations are executed automatically through `entrypoint.sh` before Uvicorn starts:

```text
Container starts
      │
      ▼
alembic upgrade head
      │
      ▼
Database schema updated
      │
      ▼
Uvicorn starts
```

---

# Docker

The application is containerized using Docker.

## Build the image

```bash
docker build -t financial-management-api .
```

## Run with Docker Compose

For the test environment:

```bash
ENV_FILE=.env.test docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

---

# Testing

The project uses **Pytest** for automated testing.

Integration tests are located in:

```text
tests/integration/
```

Current test coverage includes:

* Authentication
* Users
* Categories
* Transactions
* Dashboard
* Health Check
* Prometheus metrics

Run the complete test suite through Docker:

```bash
ENV_FILE=.env.test docker compose run --rm api pytest -v
```

The test environment uses a dedicated PostgreSQL configuration defined in `.env.test`.

---

# Code Quality & Security

The CI pipeline performs automated code quality and security checks.

## Ruff

Ruff is used for Python linting:

```bash
ruff check .
```

## Bandit

Bandit performs static security analysis:

```bash
bandit -r app -ll
```

## pip-audit

pip-audit checks project dependencies for known vulnerabilities:

```bash
pip-audit -r requirements.txt
```

These checks are executed automatically through GitHub Actions.

---

# CI/CD Pipeline

The project implements an automated CI/CD pipeline using **GitHub Actions**.

```mermaid
flowchart LR
    Push[Git Push]
    Lint[Lint]
    Tests[Unit Tests]
    Integration[Integration Tests]
    Security[Security Checks]
    Build[Docker Build]
    Registry[Push to GHCR]
    Deploy[Deploy to Render]

    Push --> Lint
    Lint --> Tests
    Tests --> Integration
    Integration --> Security
    Security --> Build
    Build --> Registry
    Registry --> Deploy
```

The pipeline performs the following stages:

1. Checkout source code
2. Run Ruff
3. Build Docker test environment
4. Run tests
5. Run integration tests
6. Run pip-audit
7. Run Bandit
8. Build production Docker image
9. Push image to GitHub Container Registry
10. Trigger Render deployment

Workflow file:

```text
.github/workflows/ci.yml
```

The deployment stage is configured to run when changes are pushed to the deployment branch after the previous pipeline stages succeed.

---

# GitHub Container Registry

Production Docker images are published to **GitHub Container Registry (GHCR)**.

The pipeline publishes:

```text
<image>:<commit-sha>
<image>:latest
```

The commit SHA tag provides an immutable reference to the source revision associated with a specific image.

---

# Deployment

The application is deployed to **Render**.

Production URL:

```text
https://financial-management-api-8h37.onrender.com
```

Production validation endpoints:

```text
GET /
GET /health
GET /metrics/
```

Example:

```bash
curl -i https://financial-management-api-8h37.onrender.com/health
```

Expected response:

```json
{
  "status": "ok"
}
```

Prometheus metrics:

```bash
curl -i https://financial-management-api-8h37.onrender.com/metrics/
```

The production `/metrics/` endpoint exposes application and Python process metrics.

---

# Environment Variables

The application uses environment variables for configuration.

Example:

```env
DATABASE_URL=postgresql://user:password@host:5432/database
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

The repository provides:

```text
.env.example
```

as a configuration reference.

> **Never commit real database credentials, JWT secrets, API keys, or other sensitive values to the repository.**

---

# Local Development

## 1. Clone the repository

```bash
git clone https://github.com/vicvictorius/Financial-management-api.git
cd Financial-management-api
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

```bash
cp .env.example .env
```

Configure the variables according to your local environment.

## 5. Run database migrations

```bash
alembic upgrade head
```

## 6. Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

### OpenAPI Schema

```text
http://localhost:8000/openapi.json
```

The same documentation is available in production:

```text
https://financial-management-api-8h37.onrender.com/docs
```

---

# Production Validation

The production environment has been validated through the following endpoints:

```text
GET /
GET /health
GET /metrics/
```

The health endpoint returns:

```json
{
  "status": "ok"
}
```

The metrics endpoint returns Prometheus-compatible metrics including:

```text
http_requests_total
http_request_duration_seconds
python_info
process_virtual_memory_bytes
process_resident_memory_bytes
```

This confirms that the API is running and that application-level observability is active in the deployed environment.

---

# Security

Security-related practices implemented in the project include:

* JWT authentication
* Password hashing
* User-level data isolation
* Environment-based secret configuration
* Pydantic request validation
* Bandit static security analysis
* Dependency vulnerability auditing
* Protected transaction and dashboard endpoints

Additional security information is available in:

```text
SECURITY.md
```

---

# Project Status

Current implementation includes:

* [x] REST API
* [x] FastAPI
* [x] PostgreSQL
* [x] SQLAlchemy
* [x] Alembic migrations
* [x] JWT authentication
* [x] User management
* [x] Category management
* [x] Transaction CRUD
* [x] Financial dashboard
* [x] Automated tests
* [x] Docker
* [x] Docker Compose
* [x] GitHub Actions CI/CD
* [x] Ruff linting
* [x] Bandit security scanning
* [x] pip-audit dependency auditing
* [x] GitHub Container Registry
* [x] Automated Render deployment
* [x] Health Check
* [x] Prometheus metrics
* [x] Production observability

---

# Future Improvements

Potential future improvements include:

* Pagination for transaction endpoints
* Advanced transaction filtering
* Date-range filtering
* Recurring transactions
* Budget management
* Expanded dashboard analytics
* Prometheus + Grafana dashboards
* Rate limiting
* API versioning
* Expanded automated test coverage
* Production alerting

---

# Author

**vicvictorius**

Backend/API project focused on **Python, FastAPI, PostgreSQL, authentication, automated testing, CI/CD, Docker, cloud deployment, and observability**.

---

## License

This project is intended for educational and portfolio purposes.
