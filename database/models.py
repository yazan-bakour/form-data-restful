from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSON
from database.connection import Base
import uuid
from datetime import datetime, timezone

CASCADE_DELETE = "all, delete-orphan"
FORM_DATA_FK = "form_data.id"

def utc_now():
    return datetime.now(timezone.utc)

class FormDataModel(Base):
    """
    SQLAlchemy model for FormData table.
    Maps to the FormData Pydantic schema.
    """
    __tablename__ = "form_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    mobile_number = Column(String(20), nullable=False)
    date_of_birth = Column(String(10), nullable=False)
    street_address = Column(Text, nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)
    title = Column(String(10), nullable=True)
    marital_status = Column(String(20), nullable=True)
    developer = Column(String(255), default="")
    job = Column(String(255), default="")

    portfolio_website = Column(String(500), default="")
    github_url = Column(String(500), default="")
    linkedin_url = Column(String(500), default="")

    preferred_work_type = Column(String(20), nullable=True)
    expected_salary = Column(String(50), default="")
    preferred_location = Column(String(255), default="")
    availability_date = Column(String(10), default="")
    career_goals = Column(Text, default="")

    professional_summary = Column(Text, default="")
    hobbies = Column(Text, default="")
    volunteer_work = Column(Text, default="")
    additional_notes = Column(Text, default="")

    created_at = Column(DateTime, default=utc_now)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)

    educations = relationship("EducationModel", back_populates="form_data", cascade=CASCADE_DELETE)
    job_experiences = relationship("JobExperienceModel", back_populates="form_data", cascade=CASCADE_DELETE)
    skills = relationship("SkillModel", back_populates="form_data", cascade=CASCADE_DELETE)
    certifications = relationship("CertificationModel", back_populates="form_data", cascade=CASCADE_DELETE)
    languages = relationship("LanguageModel", back_populates="form_data", cascade=CASCADE_DELETE)
    projects = relationship("ProjectModel", back_populates="form_data", cascade=CASCADE_DELETE)
    references = relationship("ReferenceModel", back_populates="form_data", cascade=CASCADE_DELETE)

class EducationModel(Base):
    """SQLAlchemy model for Education table."""
    __tablename__ = "educations"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey(FORM_DATA_FK), nullable=False)
    university_name = Column(String(255), nullable=False)
    degree_type = Column(String(50), nullable=True)
    course_name = Column(String(255), nullable=False)
    
    form_data = relationship("FormDataModel", back_populates="educations")

class JobExperienceModel(Base):
    """SQLAlchemy model for JobExperience table."""
    __tablename__ = "job_experiences"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey("form_data.id"), nullable=False)
    job_title = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    start_date = Column(String(10), nullable=False)
    end_date = Column(String(10), nullable=False)
    is_present_job = Column(Boolean, default=False)
    description = Column(Text, default="")

    form_data = relationship("FormDataModel", back_populates="job_experiences")

class SkillModel(Base):
    """SQLAlchemy model for Skill table."""
    __tablename__ = "skills"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey("form_data.id"), nullable=False)
    name = Column(String(255), nullable=False)
    level = Column(String(50), nullable=True)
    category = Column(String(255), nullable=False)
    
    form_data = relationship("FormDataModel", back_populates="skills")

class CertificationModel(Base):
    """SQLAlchemy model for Certification table."""
    __tablename__ = "certifications"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey("form_data.id"), nullable=False)
    name = Column(String(255), nullable=False)
    issuer = Column(String(255), nullable=False)
    date_obtained = Column(String(10), nullable=False)
    expiry_date = Column(String(10), nullable=False)
    has_expiry = Column(Boolean, default=True)
    
    form_data = relationship("FormDataModel", back_populates="certifications")

class LanguageModel(Base):
    """SQLAlchemy model for Language table."""
    __tablename__ = "languages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey("form_data.id"), nullable=False)
    name = Column(String(255), nullable=False)
    proficiency = Column(String(50), nullable=True)
    
    form_data = relationship("FormDataModel", back_populates="languages")

class ProjectModel(Base):
    """SQLAlchemy model for Project table."""
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey("form_data.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, default="")
    technologies = Column(Text, default="")
    link = Column(String(500), default="")
    start_date = Column(String(10), nullable=False)
    end_date = Column(String(10), nullable=False)
    is_ongoing = Column(Boolean, default=False)

    form_data = relationship("FormDataModel", back_populates="projects")

class ReferenceModel(Base):
    """SQLAlchemy model for Reference table."""
    __tablename__ = "references"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_data_id = Column(UUID(as_uuid=True), ForeignKey("form_data.id"), nullable=False)
    name = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)

    form_data = relationship("FormDataModel", back_populates="references")
