import pytest
from pydantic import ValidationError
from models.schemas import FormData, Education, JobExperience, Skill, Language
from models.enums import Title, MaritalStatus, DegreeType, SkillLevel, ProficiencyLevel
from models.response_schemas import FormDataResponse, EducationResponse


class TestPydanticSchemas:
    """Test suite for Pydantic schemas and validation."""

    @pytest.mark.unit
    def test_form_data_valid_creation(self):
        """Test valid FormData creation."""
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
            country="USA"
        )
        
        assert form_data.first_name == "John"
        assert form_data.last_name == "Doe"
        assert form_data.email == "john.doe@example.com"

    @pytest.mark.unit
    def test_form_data_with_enums(self):
        """Test FormData creation with enum values."""
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
            marital_status=MaritalStatus.SINGLE
        )
        
        assert form_data.title == Title.MR
        assert form_data.marital_status == MaritalStatus.SINGLE

    @pytest.mark.unit
    def test_form_data_enum_string_values(self):
        """Test FormData creation with enum string values."""
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
            title="Mr",
            marital_status="Single"
        )
        
        assert form_data.title == "Mr"
        assert form_data.marital_status == "Single"

    @pytest.mark.unit
    def test_form_data_missing_required_fields(self):
        """Test FormData validation with missing required fields."""
        with pytest.raises(ValidationError) as exc_info:
            FormData(
                first_name="John",
            )
        
        errors = exc_info.value.errors()
        required_fields = [error["loc"][0] for error in errors if error["type"] == "missing"]
        assert "last_name" in required_fields
        assert "email" in required_fields

    @pytest.mark.unit
    def test_form_data_field_validation(self):
        """Test FormData field validation."""

        with pytest.raises(ValidationError):
            FormData(
                first_name="",
                last_name="Doe",
                email="john.doe@example.com",
                mobile_number="+1234567890",
                date_of_birth="1990-01-01",
                street_address="123 Main St",
                city="Anytown",
                state="NY",
                postal_code="12345",
                country="USA"
            )

    @pytest.mark.unit
    def test_education_schema(self):
        """Test Education schema validation."""
        education = Education(
            id="edu1",
            university_name="Test University",
            degree_type=DegreeType.BACHELOR,
            course_name="Computer Science"
        )
        
        assert education.university_name == "Test University"
        assert education.degree_type == DegreeType.BACHELOR
        assert education.course_name == "Computer Science"

    @pytest.mark.unit
    def test_education_invalid_data(self):
        """Test Education schema with invalid data."""
        with pytest.raises(ValidationError):
            Education(
                id="edu1",
                university_name="",
                course_name="Computer Science"
            )

    @pytest.mark.unit
    def test_job_experience_schema(self):
        """Test JobExperience schema validation."""
        job_exp = JobExperience(
            id="job1",
            job_title="Software Developer",
            company_name="Tech Corp",
            start_date="2020-01-01",
            end_date="2023-12-31",
            is_present_job=False,
            description="Developed applications"
        )
        
        assert job_exp.job_title == "Software Developer"
        assert job_exp.company_name == "Tech Corp"
        assert job_exp.is_present_job is False

    @pytest.mark.unit
    def test_skill_schema(self):
        """Test Skill schema validation."""
        skill = Skill(
            id="skill1",
            name="Python",
            level=SkillLevel.EXPERT,
            category="Programming"
        )
        
        assert skill.name == "Python"
        assert skill.level == SkillLevel.EXPERT
        assert skill.category == "Programming"

    @pytest.mark.unit
    def test_language_schema(self):
        """Test Language schema validation."""
        language = Language(
            id="lang1",
            name="English",
            proficiency=ProficiencyLevel.NATIVE
        )
        
        assert language.name == "English"
        assert language.proficiency == ProficiencyLevel.NATIVE

    @pytest.mark.unit
    def test_form_data_with_relationships(self):
        """Test FormData with related objects."""
        education = Education(
            id="edu1",
            university_name="Test University",
            degree_type="Bachelor's Degree",
            course_name="Computer Science"
        )
        
        skill = Skill(
            id="skill1",
            name="Python",
            level="Expert",
            category="Programming"
        )
        
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
            educations=[education],
            skills=[skill]
        )
        
        assert len(form_data.educations) == 1
        assert len(form_data.skills) == 1
        assert form_data.educations[0].university_name == "Test University"
        assert form_data.skills[0].name == "Python"

    @pytest.mark.unit
    def test_response_schema_creation(self):
        """Test response schema creation."""
        response = FormDataResponse(
            id="test-id",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            mobile_number="+1234567890",
            date_of_birth="1990-01-01",
            street_address="123 Main St",
            city="Anytown",
            state="NY",
            postal_code="12345",
            country="USA"
        )
        
        assert response.id == "test-id"
        assert response.first_name == "John"
        assert response.last_name == "Doe"

    @pytest.mark.unit
    def test_response_schema_with_relationships(self):
        """Test response schema with related objects."""
        education_response = EducationResponse(
            id="edu1",
            university_name="Test University",
            degree_type="Bachelor's Degree",
            course_name="Computer Science"
        )
        
        response = FormDataResponse(
            id="test-id",
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
            educations=[education_response]
        )
        
        assert len(response.educations) == 1
        assert response.educations[0].university_name == "Test University"
