# Form Data API

A RESTful API service built with FastAPI that manages form submission data with standardized response formats, type safety, and clean architecture patterns.

## 🚀 Overview

This API provides comprehensive form data management capabilities including:
- **CRUD Operations**: Create, read, update, and delete form submissions
- **Advanced Search**: Multi-criteria filtering and search functionality
- **Data Validation**: Strong type safety using Pydantic models and enums
- **Standardized Responses**: Consistent JSON response format across all endpoints
- **Clean Architecture**: Repository-Service-Mapper pattern for maintainable code

## 🛠 Technology Stack

### Core Framework
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.12+** - Programming language
- **Pydantic** - Data validation and serialization using Python type annotations

### Database & ORM
- **SQLAlchemy** - Python SQL toolkit and Object-Relational Mapping (ORM)
- **PostgreSQL/SQLite** - Flexible database support (configurable via environment)

### Development & Testing
- **pytest** - Testing framework with async support
- **python-dotenv** - Environment variable management
- **CORS Middleware** - Cross-origin resource sharing support

### Architecture Pattern
- **Clean Architecture**: Separation of concerns with distinct layers
  - **Routes**: API endpoint definitions
  - **Services**: Business logic and data processing
  - **Repositories**: Data access layer
  - **Mappers**: Data transformation between layers
  - **Models**: Database models and response schemas

## 📁 Project Structure

```
├── database/           # Database configuration and models
├── models/            # Pydantic schemas and enums
├── routes/            # FastAPI route definitions
├── services/          # Business logic layer
│   ├── mappers/       # Data transformation utilities
│   └── repositories/  # Data access layer
├── tests/             # Test suite
├── utils/             # Response helpers and utilities
├── main.py            # FastAPI application entry point
├── run_server.py      # Development server runner
└── pyproject.toml     # Project configuration
```

## ⚙️ Environment Setup

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the project root by copying the example:

```bash
cp .env.example .env
```

Configure the following environment variables in your `.env` file:

#### Required Variables

```bash
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
# Or for SQLite (development):
# DATABASE_URL=sqlite:///./formdata.db

# API Configuration
API_TITLE=Form Data API
API_VERSION=1.0.0
DEBUG=true

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

#### Database URL Examples

**PostgreSQL (Production):**
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/formdata_db
```

**SQLite (Development):**
```bash
DATABASE_URL=sqlite:///./formdata.db
```

**PostgreSQL with SSL:**
```bash
DATABASE_URL=postgresql://username:password@host:5432/database?sslmode=require
```

### 3. Database Setup

The application will automatically create database tables on startup using SQLAlchemy's `create_all()` method.

For PostgreSQL, ensure your database exists:
```sql
CREATE DATABASE formdata_db;
```

## 🚦 Running the Application

### Development Server

```bash
# Using the run script
python run_server.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📊 API Documentation

Once running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test categories
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only
```

## 📋 API Response Format

All API responses follow a standardized format:

```json
{
  "success": boolean,
  "message": string,
  "data": object | null,
  "errors": Record<string, string | string[]> | null
}
```

### Success Response Example
```json
{
  "success": true,
  "message": "Form data retrieved successfully",
  "data": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "John Doe",
    "email": "john@example.com"
  },
  "errors": null
}
```

### Error Response Example
```json
{
  "success": false,
  "message": "Validation failed",
  "data": null,
  "errors": {
    "email": "Invalid email format",
    "age": "Must be between 18 and 120"
  }
}
```

## 🔧 Configuration Options

### Environment Variables Reference

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `DATABASE_URL` | Database connection string | **Required** | `postgresql://user:pass@host:5432/db` |
| `API_TITLE` | API title in documentation | `My API Server` | `Form Data API` |
| `API_VERSION` | API version | `1.0.0` | `1.2.0` |
| `DEBUG` | Enable debug mode | `false` | `true` |
| `HOST` | Server host | `0.0.0.0` | `127.0.0.1` |
| `PORT` | Server port | `8000` | `3000` |

## 🏗 Architecture Highlights

### Type Safety
- Elimination of `Any` types in favor of specific Pydantic models
- Enum-based field validation (Education, Skills, Languages, etc.)
- Strict response typing with `ApiResponse[T]` generics

### Clean Architecture
- **Repository Pattern**: Data access abstraction
- **Service Layer**: Business logic separation  
- **Mapper Pattern**: Data transformation utilities
- **Response Helpers**: Consistent API response formatting

### Error Handling
- Comprehensive exception handling
- Standardized error responses
- Proper HTTP status codes
- Detailed validation error messages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.