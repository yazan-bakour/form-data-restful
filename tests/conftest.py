import pytest
import asyncio
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database.connection import Base, get_db
from database.models import FormDataModel
from models.schemas import FormData

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override database dependency for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database session for each test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client with test database."""
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_form_data():
    """Sample form data for testing."""
    return {
        "title": "Mr",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "mobile_number": "+1234567890",
        "date_of_birth": "1990-01-01",
        "street_address": "123 Main St",
        "city": "Anytown",
        "state": "NY",
        "postal_code": "12345",
        "country": "USA",
        "marital_status": "Single",
        "developer": "Full Stack Developer",
        "job": "Software Engineer",
        "languages": [
            {
                "id": "lang1",
                "name": "English",
                "proficiency": "Native"
            },
            {
                "id": "lang2", 
                "name": "Spanish",
                "proficiency": "Conversational"
            }
        ],
        "educations": [
            {
                "id": "edu1",
                "university_name": "University of Example",
                "degree_type": "Bachelor's Degree",
                "course_name": "Computer Science"
            }
        ],
        "job_experiences": [
            {
                "id": "job1",
                "job_title": "Software Developer",
                "company_name": "Tech Corp",
                "start_date": "2020-01-01",
                "end_date": "2023-12-31",
                "is_present_job": False,
                "description": "Developed web applications"
            }
        ],
        "skills": [
            {
                "id": "skill1",
                "name": "Python",
                "level": "Expert",
                "category": "Programming"
            }
        ],
        "certifications": [],
        "projects": [],
        "references": []
    }


@pytest.fixture
def sample_invalid_form_data():
    """Invalid form data for testing validation."""
    return {
        "first_name": "",
        "email": "invalid-email",
        "mobile_number": "+1234567890",
        "date_of_birth": "1990-01-01",
        "street_address": "123 Main St",
        "city": "Anytown",
        "state": "NY",
        "postal_code": "12345",
        "country": "USA"
    }


@pytest.fixture
def created_form_data(client, sample_form_data):
    """Create a form data entry and return its ID."""
    response = client.post("/api/v1/form-data/", json=sample_form_data)
    assert response.status_code == 201
    return response.json()["data"]["id"]
