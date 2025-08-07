import pytest
from models.enums import Title, MaritalStatus, DegreeType, SkillLevel, ProficiencyLevel, WorkType


class TestEnums:
    """Test suite for enum definitions."""

    @pytest.mark.unit
    def test_title_enum_values(self):
        """Test Title enum values."""
        assert Title.MR == "Mr"
        assert Title.MRS == "Mrs"
        assert Title.MISS == "Miss"
        assert Title.DR == "Dr"
        
        all_titles = [Title.MR, Title.MRS, Title.MISS, Title.DR]
        assert len(all_titles) == 4

    @pytest.mark.unit
    def test_marital_status_enum_values(self):
        """Test MaritalStatus enum values."""
        assert MaritalStatus.SINGLE == "Single"
        assert MaritalStatus.MARRIED == "Married"
        assert MaritalStatus.DIVORCED == "Divorced"
        assert MaritalStatus.WIDOWED == "Widowed"
        assert MaritalStatus.SEPARATED == "Separated"
        
        all_statuses = [
            MaritalStatus.SINGLE, MaritalStatus.MARRIED, MaritalStatus.DIVORCED,
            MaritalStatus.WIDOWED, MaritalStatus.SEPARATED
        ]
        assert len(all_statuses) == 5

    @pytest.mark.unit
    def test_degree_type_enum_values(self):
        """Test DegreeType enum values."""
        assert DegreeType.BACHELOR == "Bachelor's Degree"
        assert DegreeType.MASTER == "Master's Degree"
        assert DegreeType.PHD == "PhD"
        assert DegreeType.DIPLOMA == "Diploma"
        assert DegreeType.CERTIFICATE == "Certificate"
        assert DegreeType.ASSOCIATE == "Associate Degree"
        
        all_degrees = [
            DegreeType.BACHELOR, DegreeType.MASTER, DegreeType.PHD,
            DegreeType.DIPLOMA, DegreeType.CERTIFICATE, DegreeType.ASSOCIATE
        ]
        assert len(all_degrees) == 6

    @pytest.mark.unit
    def test_skill_level_enum_values(self):
        """Test SkillLevel enum values."""
        assert SkillLevel.BEGINNER == "Beginner"
        assert SkillLevel.INTERMEDIATE == "Intermediate"
        assert SkillLevel.ADVANCED == "Advanced"
        assert SkillLevel.EXPERT == "Expert"
        
        all_levels = [
            SkillLevel.BEGINNER, SkillLevel.INTERMEDIATE,
            SkillLevel.ADVANCED, SkillLevel.EXPERT
        ]
        assert len(all_levels) == 4

    @pytest.mark.unit
    def test_proficiency_level_enum_values(self):
        """Test ProficiencyLevel enum values."""
        assert ProficiencyLevel.BASIC == "Basic"
        assert ProficiencyLevel.CONVERSATIONAL == "Conversational"
        assert ProficiencyLevel.FLUENT == "Fluent"
        assert ProficiencyLevel.NATIVE == "Native"
        
        all_proficiencies = [
            ProficiencyLevel.BASIC, ProficiencyLevel.CONVERSATIONAL,
            ProficiencyLevel.FLUENT, ProficiencyLevel.NATIVE
        ]
        assert len(all_proficiencies) == 4

    @pytest.mark.unit
    def test_work_type_enum_values(self):
        """Test WorkType enum values."""
        assert WorkType.REMOTE == "Remote"
        assert WorkType.ONSITE == "On-site"
        assert WorkType.HYBRID == "Hybrid"
        assert WorkType.ANY == "Any"
        
        all_work_types = [
            WorkType.REMOTE, WorkType.ONSITE, WorkType.HYBRID, WorkType.ANY
        ]
        assert len(all_work_types) == 4

    @pytest.mark.unit
    def test_enum_inheritance(self):
        """Test that enums inherit from str."""
        assert isinstance(Title.MR, str)
        assert isinstance(MaritalStatus.SINGLE, str)
        assert isinstance(DegreeType.BACHELOR, str)
        assert isinstance(SkillLevel.EXPERT, str)
        assert isinstance(ProficiencyLevel.NATIVE, str)
        assert isinstance(WorkType.REMOTE, str)

    @pytest.mark.unit
    def test_enum_comparison(self):
        """Test enum comparison with strings."""
        assert Title.MR == "Mr"
        assert MaritalStatus.SINGLE == "Single"
        assert DegreeType.BACHELOR == "Bachelor's Degree"
        
        assert Title.MR != "Mrs"
        assert MaritalStatus.SINGLE != "Married"

    @pytest.mark.unit
    def test_enum_in_collections(self):
        """Test enum usage in collections."""
        titles = [Title.MR, Title.MRS]
        assert "Mr" in titles
        assert "Mrs" in titles
        assert "Dr" not in titles[:2]

    @pytest.mark.unit
    def test_enum_iteration(self):
        """Test enum iteration."""
        title_values = [title.value for title in Title]
        expected_titles = ["Mr", "Mrs", "Miss", "Dr"]
        assert set(title_values) == set(expected_titles)
        
        status_values = [status.value for status in MaritalStatus]
        expected_statuses = ["Single", "Married", "Divorced", "Widowed", "Separated"]
        assert set(status_values) == set(expected_statuses)
