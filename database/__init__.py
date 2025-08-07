from .connection import engine, SessionLocal, get_db, Base
from .models import (
    FormDataModel,
    EducationModel,
    JobExperienceModel,
    SkillModel,
    CertificationModel,
    LanguageModel,
    ProjectModel,
    ReferenceModel
)

def create_tables():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """Drop all database tables."""
    Base.metadata.drop_all(bind=engine)

__all__ = [
    "engine",
    "SessionLocal", 
    "get_db",
    "Base",
    "FormDataModel",
    "EducationModel",
    "JobExperienceModel", 
    "SkillModel",
    "CertificationModel",
    "LanguageModel",
    "ProjectModel",
    "ReferenceModel"
]
