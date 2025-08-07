from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional, Generic, TypeVar, Any
from datetime import datetime
from .enums import Title, MaritalStatus, DegreeType, SkillLevel, ProficiencyLevel, WorkType

T = TypeVar('T')

class CreateResponse(BaseModel):
    """Response model for creation operations"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str

class StorageInfoResponse(BaseModel):
    """Response model for storage information"""
    model_config = ConfigDict(from_attributes=True)
    
    total_entries: int
    storage_type: str
    database_engine: str

class ApiResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(from_attributes=True)
    
    success: bool = Field(default=True)
    data: Optional[T] = Field(default=None)
    error: Optional[str] = Field(default=None)
    message: Optional[str] = Field(default=None)
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    
    def __init__(self, data: Optional[T] = None, error: Optional[str] = None, message: Optional[str] = None, **kwargs):
        """
        Smart constructor that automatically determines success/error based on provided fields.
        """
        if error is not None:
            super().__init__(
                success=False,
                data=None,
                error=error,
                message=message or "An error occurred",
                **kwargs
            )
        else:
            super().__init__(
                success=True,
                data=data,
                error=None,
                message=None,
                **kwargs
            )


class EducationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    university_name: str
    degree_type: Optional[DegreeType] = None
    course_name: str


class JobExperienceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    job_title: str
    company_name: str
    start_date: str
    end_date: str
    is_present_job: bool = False
    description: str = ""


class SkillResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    name: str
    level: Optional[SkillLevel] = None
    category: str


class CertificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    name: str
    issuer: str
    date_obtained: str
    expiry_date: str
    has_expiry: bool = True


class LanguageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    name: str
    proficiency: Optional[ProficiencyLevel] = None


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    title: str
    description: str = ""
    technologies: str = ""
    link: str = ""
    start_date: str
    end_date: str
    is_ongoing: bool = False


class ReferenceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    name: str
    position: str
    company: str
    email: str
    phone: str


class FormDataResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    date_of_birth: str
    street_address: str
    city: str
    state: str
    postal_code: str
    country: str
    title: Optional[Title] = None
    marital_status: Optional[MaritalStatus] = None
    developer: str = ""
    job: str = ""
    portfolio_website: str = ""
    github_url: str = ""
    linkedin_url: str = ""
    preferred_work_type: Optional[WorkType] = None
    expected_salary: str = ""
    preferred_location: str = ""
    availability_date: str = ""
    career_goals: str = ""
    professional_summary: str = ""
    hobbies: str = ""
    volunteer_work: str = ""
    additional_notes: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    educations: List[EducationResponse] = []
    job_experiences: List[JobExperienceResponse] = []
    skills: List[SkillResponse] = []
    certifications: List[CertificationResponse] = []
    languages: List[LanguageResponse] = []
    projects: List[ProjectResponse] = []
    references: List[ReferenceResponse] = []
