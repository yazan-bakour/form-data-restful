import pytest
from fastapi.testclient import TestClient
import uuid


class TestFormDataAPI:
    """Test suite for Form Data API endpoints."""

    @pytest.mark.unit
    def test_create_form_data_success(self, client, sample_form_data):
        """Test successful form data creation."""
        response = client.post("/api/v1/form-data/", json=sample_form_data)
        
        assert response.status_code == 201
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert "id" in data["data"]
        
        created_id = data["data"]["id"]
        assert uuid.UUID(created_id)

    @pytest.mark.unit
    def test_create_form_data_with_relationships(self, client, sample_form_data):
        """Test form data creation with related records - just verify creation success."""
        response = client.post("/api/v1/form-data/", json=sample_form_data)
        
        assert response.status_code == 201
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert "id" in data["data"]
        
        created_id = data["data"]["id"]
        assert uuid.UUID(created_id)

    @pytest.mark.unit
    def test_create_form_data_missing_required_fields(self, client):
        """Test form data creation with missing required fields."""
        incomplete_data = {
            "first_name": "John",

        }
        
        response = client.post("/api/v1/form-data/", json=incomplete_data)
        assert response.status_code == 422

    @pytest.mark.unit
    def test_create_form_data_invalid_enum_values(self, client):
        """Test form data creation with invalid enum values."""
        invalid_data = {
            "title": "InvalidTitle",
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
            "marital_status": "InvalidStatus",
        }
        
        response = client.post("/api/v1/form-data/", json=invalid_data)
        assert response.status_code == 422

    @pytest.mark.unit
    def test_get_form_data_by_id_success(self, client, created_form_data):
        """Test successful retrieval of form data by ID."""
        form_id = created_form_data
        response = client.get(f"/api/v1/form-data/{form_id}")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert isinstance(data["data"], dict)
        assert data["data"]["id"] == form_id
        assert "first_name" in data["data"]

    @pytest.mark.unit
    def test_get_form_data_by_id_not_found(self, client):
        """Test retrieval of non-existent form data."""
        non_existent_id = str(uuid.uuid4())
        response = client.get(f"/api/v1/form-data/{non_existent_id}")
        
        assert response.status_code == 404
        data = response.json()
        
        assert data["success"] is False
        assert "message" in data
        assert "errors" in data

    @pytest.mark.unit
    def test_get_form_data_by_invalid_id(self, client):
        """Test retrieval with invalid UUID format."""
        invalid_id = "not-a-valid-uuid"
        response = client.get(f"/api/v1/form-data/{invalid_id}")
        
        assert response.status_code == 404
        data = response.json()
        
        assert data["success"] is False
        assert "message" in data
        assert "errors" in data

    @pytest.mark.unit
    def test_get_all_form_data_empty(self, client):
        """Test retrieval of all form data when database is empty."""
        response = client.get("/api/v1/form-data/")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) == 0

    @pytest.mark.unit
    def test_get_all_form_data_with_records(self, client, sample_form_data):
        """Test retrieval of all form data with existing records."""
        client.post("/api/v1/form-data/", json=sample_form_data)
        
        sample_form_data_2 = sample_form_data.copy()
        sample_form_data_2["first_name"] = "Jane"
        sample_form_data_2["email"] = "jane.doe@example.com"
        client.post("/api/v1/form-data/", json=sample_form_data_2)
        
        response = client.get("/api/v1/form-data/")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) == 2
        assert all(isinstance(item, dict) for item in data["data"])

    @pytest.mark.unit
    def test_update_form_data_success(self, client, created_form_data, sample_form_data):
        """Test successful form data update."""
        form_id = created_form_data
        
        updated_data = sample_form_data.copy()
        updated_data["first_name"] = "Updated John"
        updated_data["job"] = "Senior Software Engineer"
        
        response = client.put(f"/api/v1/form-data/{form_id}", json=updated_data)
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert data["data"]["first_name"] == "Updated John"
        assert data["data"]["job"] == "Senior Software Engineer"

    @pytest.mark.unit
    def test_update_form_data_not_found(self, client, sample_form_data):
        """Test update of non-existent form data."""
        non_existent_id = str(uuid.uuid4())
        response = client.put(f"/api/v1/form-data/{non_existent_id}", json=sample_form_data)
        
        assert response.status_code == 404
        data = response.json()
        
        assert data["success"] is False
        assert "message" in data
        assert "errors" in data

    @pytest.mark.unit
    def test_delete_form_data_success(self, client, created_form_data):
        """Test successful form data deletion."""
        form_id = created_form_data
        
        response = client.delete(f"/api/v1/form-data/{form_id}")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert data["data"]["id"] == form_id
        assert "first_name" in data["data"]
        
        get_response = client.get(f"/api/v1/form-data/{form_id}")
        assert get_response.status_code == 404

    @pytest.mark.unit
    def test_delete_form_data_not_found(self, client):
        """Test deletion of non-existent form data."""
        non_existent_id = str(uuid.uuid4())
        response = client.delete(f"/api/v1/form-data/{non_existent_id}")
        
        assert response.status_code == 404
        data = response.json()
        
        assert data["success"] is False
        assert "message" in data
        assert "errors" in data

    @pytest.mark.unit
    def test_search_form_data_by_name(self, client, sample_form_data):
        """Test search functionality by name."""
        client.post("/api/v1/form-data/", json=sample_form_data)
        
        response = client.get("/api/v1/form-data/search?first_name=John")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) == 1
        assert data["data"][0]["first_name"] == "John"

    @pytest.mark.unit
    def test_search_form_data_no_results(self, client):
        """Test search with no matching results."""
        response = client.get("/api/v1/form-data/search?first_name=NonExistent")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["success"] is True
        assert "message" in data
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) == 0

    @pytest.mark.integration
    def test_full_crud_workflow(self, client, sample_form_data):
        """Test complete CRUD workflow."""
        create_response = client.post("/api/v1/form-data/", json=sample_form_data)
        assert create_response.status_code == 201
        form_id = create_response.json()["data"]["id"]
        
        read_response = client.get(f"/api/v1/form-data/{form_id}")
        assert read_response.status_code == 200
        
        updated_data = sample_form_data.copy()
        updated_data["first_name"] = "Updated Name"
        update_response = client.put(f"/api/v1/form-data/{form_id}", json=updated_data)
        assert update_response.status_code == 200
        
        read_updated_response = client.get(f"/api/v1/form-data/{form_id}")
        assert read_updated_response.status_code == 200
        updated_json = read_updated_response.json()
        assert updated_json["success"] is True
        assert updated_json["data"]["first_name"] == "Updated Name"
        
        delete_response = client.delete(f"/api/v1/form-data/{form_id}")
        assert delete_response.status_code == 200
        
        read_deleted_response = client.get(f"/api/v1/form-data/{form_id}")
        assert read_deleted_response.status_code == 404
