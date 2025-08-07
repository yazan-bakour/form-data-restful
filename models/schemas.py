from pydantic import BaseModel, Field, validator, ConfigDict
from typing import List, Optional
from datetime import date
from .enums import (
    Title, MaritalStatus, DegreeType, SkillLevel, 
    ProficiencyLevel, WorkType
)

DATE_FORMAT_DESC = "Date in YYYY-MM-DD format"


class Education(BaseModel):
    id: str
    university_name: str = Field(..., min_length=1)
    degree_type: Optional[DegreeType] = None
    course_name: str = Field(..., min_length=1)

    model_config = ConfigDict(use_enum_values=True)


class JobExperience(BaseModel):
    id: str
    job_title: str = Field(..., min_length=1)
    company_name: str = Field(..., min_length=1)
    start_date: str = Field(..., description=DATE_FORMAT_DESC)
    end_date: str = Field(..., description=DATE_FORMAT_DESC)
    is_present_job: bool = False
    description: str = ""

    model_config = ConfigDict(use_enum_values=True)


class Skill(BaseModel):
    id: str
    name: str = Field(..., min_length=1)
    level: Optional[SkillLevel] = None
    category: str = Field(..., min_length=1)

    model_config = ConfigDict(use_enum_values=True)


class Certification(BaseModel):
    id: str
    name: str = Field(..., min_length=1)
    issuer: str = Field(..., min_length=1)
    date_obtained: str = Field(..., description=DATE_FORMAT_DESC)
    expiry_date: str = Field(..., description=DATE_FORMAT_DESC)
    has_expiry: bool = True

    model_config = ConfigDict(use_enum_values=True)


class Language(BaseModel):
    id: str
    name: str = Field(..., min_length=1)
    proficiency: Optional[ProficiencyLevel] = None

    model_config = ConfigDict(use_enum_values=True)


class Project(BaseModel):
    id: str
    title: str = Field(..., min_length=1)
    description: str = ""
    technologies: str = ""
    link: str = ""
    start_date: str = Field(..., description=DATE_FORMAT_DESC)
    end_date: str = Field(..., description=DATE_FORMAT_DESC)
    is_ongoing: bool = False

    model_config = ConfigDict(use_enum_values=True)


class Reference(BaseModel):
    id: str
    name: str = Field(..., min_length=1)
    position: str = Field(..., min_length=1)
    company: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)

    model_config = ConfigDict(use_enum_values=True)


class FormData(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    mobile_number: str = Field(..., min_length=1)
    date_of_birth: str = Field(..., description=DATE_FORMAT_DESC)
    street_address: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    state: str = Field(..., min_length=1)
    postal_code: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    title: Optional[Title] = None
    marital_status: Optional[MaritalStatus] = None
    developer: str = ""
    job: str = ""
    
    educations: List[Education] = []
    job_experiences: List[JobExperience] = []
    
    skills: List[Skill] = []
    certifications: List[Certification] = []
    languages: List[Language] = []
    
    projects: List[Project] = []
    portfolio_website: str = ""
    github_url: str = ""
    linkedin_url: str = ""
    references: List[Reference] = []
    
    preferred_work_type: Optional[WorkType] = None
    expected_salary: str = ""
    preferred_location: str = ""
    availability_date: str = Field("", description=DATE_FORMAT_DESC)
    career_goals: str = ""
    
    professional_summary: str = ""
    hobbies: str = ""
    volunteer_work: str = ""
    additional_notes: str = ""

    model_config = ConfigDict(
        use_enum_values=True,
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "mobile_number": "+1234567890",
                "date_of_birth": "1990-01-01",
                "street_address": "123 Main St",
                "city": "New York",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "title": "Mr",
                "marital_status": "Single",
                "developer": "Full Stack Developer",
                "job": "Software Engineer",
                "educations": [],
                "job_experiences": [],
                "skills": [],
                "certifications": [],
                "languages": [],
                "projects": [],
                "portfolio_website": "https://johndoe.dev",
                "github_url": "https://github.com/johndoe",
                "linkedin_url": "https://linkedin.com/in/johndoe",
                "references": [],
                "preferred_work_type": "Remote",
                "expected_salary": "80000",
                "preferred_location": "Remote",
                "availability_date": "2025-01-01",
                "career_goals": "Become a senior software engineer",
                "professional_summary": "Experienced developer with 5 years of experience",
                "hobbies": "Reading, Gaming",
                "volunteer_work": "Code for Good",
                "additional_notes": "Available for immediate start"
            }
        }
    )
