import pytest
from uuid import uuid4
from sqlalchemy.orm import Session
from services import FormService
from models.schemas import FormData
from models.response_schemas import FormDataResponse
from database.models import FormDataModel
from models.enums import Title, MaritalStatus


class TestFormService:
    """Test suite for FormService."""

    @pytest.fixture
    def service(self, db_session):
        """Create FormService instance with test database."""
        return FormService(db_session)

    @pytest.fixture
    def sample_pydantic_data(self):
        """Sample Pydantic FormData instance for testing."""
        return FormData(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            mobile_number="+1234567890",
            date_of_birth="1990-01-01",
            street_address="123 Main St",
            city="Anytown",
            state="NY",
            postal_code="12345",
            country="USA",
            title=Title.MR,
            marital_status=MaritalStatus.SINGLE
        )

    @pytest.mark.unit
    def test_create_form_data_success(self, service, sample_pydantic_data):
        """Test successful form data creation in service layer."""
        result = service.create_form_data(sample_pydantic_data)
        
        assert isinstance(result, FormDataResponse)
        assert result.first_name == "John"
        assert result.last_name == "Doe"
        assert result.email == "john.doe@example.com"
        assert result.title == "Mr"
        assert result.marital_status == "Single"
        assert result.id is not None

    @pytest.mark.unit
    def test_get_form_data_success(self, service, sample_pydantic_data):
        """Test successful form data retrieval."""
        create_result = service.create_form_data(sample_pydantic_data)
        form_id = create_result.id
        
        result = service.get_form_data(form_id)
        
        assert result is not None
        assert isinstance(result, FormDataResponse)
        assert result.id == form_id
        assert result.first_name == "John"
        assert result.last_name == "Doe"

    @pytest.mark.unit
    def test_get_form_data_not_found(self, service):
        """Test retrieval of non-existent form data."""
        non_existent_id = str(uuid4())
        result = service.get_form_data(non_existent_id)
        
        assert result is None

    @pytest.mark.unit
    def test_get_form_data_invalid_uuid(self, service):
        """Test retrieval with invalid UUID format."""
        invalid_id = "not-a-valid-uuid"
        result = service.get_form_data(invalid_id)
        
        assert result is None

    @pytest.mark.unit
    def test_get_all_form_data_empty(self, service):
        """Test retrieval of all form data when empty."""
        result = service.get_all_form_data()
        
        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.unit
    def test_get_all_form_data_with_records(self, service, sample_pydantic_data):
        """Test retrieval of all form data with existing records."""
        service.create_form_data(sample_pydantic_data)
        
        sample_pydantic_data.first_name = "Jane"
        sample_pydantic_data.email = "jane.doe@example.com"
        service.create_form_data(sample_pydantic_data)
        
        result = service.get_all_form_data()
        
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(item, FormDataResponse) for item in result)

    @pytest.mark.unit
    def test_update_form_data_success(self, service, sample_pydantic_data):
        """Test successful form data update."""
        create_result = service.create_form_data(sample_pydantic_data)
        form_id = create_result.id
        
        sample_pydantic_data.first_name = "Updated John"
        sample_pydantic_data.job = "Senior Developer"
        
        result = service.update_form_data(form_id, sample_pydantic_data)
        
        assert result is not None
        assert isinstance(result, FormDataResponse)
        assert result.first_name == "Updated John"
        assert result.job == "Senior Developer"

    @pytest.mark.unit
    def test_update_form_data_not_found(self, service, sample_pydantic_data):
        """Test update of non-existent form data."""
        non_existent_id = str(uuid4())
        result = service.update_form_data(non_existent_id, sample_pydantic_data)
        
        assert result is None

    @pytest.mark.unit
    def test_delete_form_data_success(self, service, sample_pydantic_data):
        """Test successful form data deletion."""
        create_result = service.create_form_data(sample_pydantic_data)
        form_id = create_result.id
        
        result = service.delete_form_data(form_id)
        
        assert result is not None
        assert isinstance(result, FormDataResponse)
        assert result.id == form_id
        
        get_result = service.get_form_data(form_id)
        assert get_result is None

    @pytest.mark.unit
    def test_delete_form_data_not_found(self, service):
        """Test deletion of non-existent form data."""
        non_existent_id = str(uuid4())
        result = service.delete_form_data(non_existent_id)
        
        assert result is None

    @pytest.mark.unit
    def test_search_form_data_by_name(self, service, sample_pydantic_data):
        """Test search functionality."""
        service.create_form_data(sample_pydantic_data)
        
        result = service.search_form_data(first_name="John")
        
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].first_name == "John"

    @pytest.mark.unit
    def test_search_form_data_no_results(self, service):
        """Test search with no matching results."""
        result = service.search_form_data(first_name="NonExistent")
        
        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.unit
    def test_get_storage_info(self, service, sample_pydantic_data):
        """Test storage info retrieval."""
        service.create_form_data(sample_pydantic_data)
        
        result = service.get_storage_info()
        
        assert isinstance(result, dict)
        assert result["total_entries"] == 1
        assert result["storage_type"] == "database"

    @pytest.mark.unit
    def test_enum_handling(self, service):
        """Test proper enum handling in service."""
        from models.enums import Title, MaritalStatus
        
        form_data = FormData(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            mobile_number="+1234567890",
            date_of_birth="1990-01-01",
            street_address="123 Main St",
            city="Anytown",
            state="NY",
            postal_code="12345",
            country="USA",
            title=Title.MR,
            marital_status=MaritalStatus.MARRIED
        )
        
        result = service.create_form_data(form_data)
        
        assert isinstance(result, FormDataResponse)
        assert result.title == "Mr"
        assert result.marital_status == "Married"
