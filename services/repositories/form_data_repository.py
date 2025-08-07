"""
Repository layer for FormData database operations.
Handles all database access and CRUD operations.
"""
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from database.models import (
    FormDataModel, EducationModel, JobExperienceModel, SkillModel,
    CertificationModel, LanguageModel, ProjectModel, ReferenceModel
)
from models.schemas import FormData
from datetime import datetime


def get_enum_value(value):
    """Helper function to safely get enum value."""
    if hasattr(value, 'value'):
        return value.value
    return value


class FormDataRepository:
    """
    Repository class for FormData database operations.
    Follows the Repository pattern for data access abstraction.
    """
    
    def __init__(self, db: Session):
        """Initialize repository with database session."""
        self.db = db
    
    def create(self, form_data: FormData) -> FormDataModel:
        """Create a new form data entry in the database."""
        try:
            db_form_data = FormDataModel(
                first_name=form_data.first_name,
                last_name=form_data.last_name,
                email=form_data.email,
                mobile_number=form_data.mobile_number,
                date_of_birth=form_data.date_of_birth,
                street_address=form_data.street_address,
                city=form_data.city,
                state=form_data.state,
                postal_code=form_data.postal_code,
                country=form_data.country,
                title=get_enum_value(form_data.title),
                marital_status=get_enum_value(form_data.marital_status),
                developer=form_data.developer,
                job=form_data.job,
                portfolio_website=form_data.portfolio_website,
                github_url=form_data.github_url,
                linkedin_url=form_data.linkedin_url,
                preferred_work_type=get_enum_value(form_data.preferred_work_type),
                expected_salary=form_data.expected_salary,
                preferred_location=form_data.preferred_location,
                availability_date=form_data.availability_date,
                career_goals=form_data.career_goals,
                professional_summary=form_data.professional_summary,
                hobbies=form_data.hobbies,
                volunteer_work=form_data.volunteer_work,
                additional_notes=form_data.additional_notes
            )
            
            self.db.add(db_form_data)
            self.db.flush()
            
            self._create_related_records(db_form_data.id, form_data)
            
            self.db.commit()
            self.db.refresh(db_form_data)
            
            return db_form_data
            
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"Error creating form data: {str(e)}")
    
    def get_by_id(self, form_id: str) -> Optional[FormDataModel]:
        """Retrieve form data by ID."""
        try:
            uuid_id = UUID(form_id)
        except ValueError:
            return None
            
        return self.db.query(FormDataModel).filter(
            FormDataModel.id == uuid_id
        ).first()
    
    def get_all(self) -> List[FormDataModel]:
        """Retrieve all form data entries."""
        return self.db.query(FormDataModel).all()
    
    def update(self, form_id: str, form_data: FormData) -> Optional[FormDataModel]:
        """Update existing form data."""
        try:
            uuid_id = UUID(form_id)
        except ValueError:
            return None
            
        db_form_data = self.db.query(FormDataModel).filter(
            FormDataModel.id == uuid_id
        ).first()
        
        if not db_form_data:
            return None
        
        try:
            db_form_data.first_name = form_data.first_name
            db_form_data.last_name = form_data.last_name
            db_form_data.email = form_data.email
            db_form_data.mobile_number = form_data.mobile_number
            db_form_data.date_of_birth = form_data.date_of_birth
            db_form_data.street_address = form_data.street_address
            db_form_data.city = form_data.city
            db_form_data.state = form_data.state
            db_form_data.postal_code = form_data.postal_code
            db_form_data.country = form_data.country
            db_form_data.title = get_enum_value(form_data.title) if form_data.title else None
            db_form_data.marital_status = get_enum_value(form_data.marital_status) if form_data.marital_status else None
            db_form_data.developer = form_data.developer
            db_form_data.job = form_data.job
            db_form_data.portfolio_website = form_data.portfolio_website
            db_form_data.github_url = form_data.github_url
            db_form_data.linkedin_url = form_data.linkedin_url
            db_form_data.preferred_work_type = get_enum_value(form_data.preferred_work_type) if form_data.preferred_work_type else None
            db_form_data.expected_salary = form_data.expected_salary
            db_form_data.preferred_location = form_data.preferred_location
            db_form_data.availability_date = form_data.availability_date
            db_form_data.career_goals = form_data.career_goals
            db_form_data.professional_summary = form_data.professional_summary
            db_form_data.hobbies = form_data.hobbies
            db_form_data.volunteer_work = form_data.volunteer_work
            db_form_data.additional_notes = form_data.additional_notes
            db_form_data.updated_at = datetime.now()
            
            self.db.commit()
            self.db.refresh(db_form_data)
            
            return db_form_data
            
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"Error updating form data: {str(e)}")
    
    def delete(self, form_id: str) -> Optional[FormDataModel]:
        """Delete form data by ID."""
        try:
            uuid_id = UUID(form_id)
        except ValueError:
            return None
            
        db_form_data = self.db.query(FormDataModel).filter(
            FormDataModel.id == uuid_id
        ).first()
        
        if not db_form_data:
            return None
        
        try:
            deleted_data = db_form_data
            
            self.db.delete(db_form_data)
            self.db.commit()
            
            return deleted_data
            
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"Error deleting form data: {str(e)}")
    
    def search(self, first_name: Optional[str] = None, last_name: Optional[str] = None,
               email: Optional[str] = None, job_title: Optional[str] = None) -> List[FormDataModel]:
        """Search form data based on criteria."""
        query = self.db.query(FormDataModel)
        
        if first_name:
            query = query.filter(FormDataModel.first_name.ilike(f"%{first_name}%"))
        if last_name:
            query = query.filter(FormDataModel.last_name.ilike(f"%{last_name}%"))
        if email:
            query = query.filter(FormDataModel.email.ilike(f"%{email}%"))
        if job_title:
            query = query.filter(FormDataModel.job.ilike(f"%{job_title}%"))
        
        return query.all()
    
    def count(self) -> int:
        """Get total count of form data entries."""
        return self.db.query(FormDataModel).count()
    
    def _create_related_records(self, form_data_id, form_data: FormData) -> None:
        """Helper method to create related records."""
        uuid_id = self._convert_to_uuid(form_data_id)
        if uuid_id is None:
            return
            
        self._create_educations(uuid_id, form_data.educations)
        self._create_job_experiences(uuid_id, form_data.job_experiences)
        self._create_skills(uuid_id, form_data.skills)
        self._create_certifications(uuid_id, form_data.certifications)
        self._create_languages(uuid_id, form_data.languages)
        self._create_projects(uuid_id, form_data.projects)
        self._create_references(uuid_id, form_data.references)
    
    def _convert_to_uuid(self, form_data_id) -> Optional[UUID]:
        """Convert form_data_id to UUID."""
        if isinstance(form_data_id, str):
            try:
                return UUID(form_data_id)
            except ValueError:
                return None
        return form_data_id
    
    def _create_educations(self, uuid_id: UUID, educations: list) -> None:
        """Create education records."""
        for edu in educations:
            db_edu = EducationModel(
                form_data_id=uuid_id,
                university_name=edu.university_name,
                degree_type=get_enum_value(edu.degree_type) if edu.degree_type else None,
                course_name=edu.course_name
            )
            self.db.add(db_edu)
    
    def _create_job_experiences(self, uuid_id: UUID, job_experiences: list) -> None:
        """Create job experience records."""
        for job_exp in job_experiences:
            db_job_exp = JobExperienceModel(
                form_data_id=uuid_id,
                job_title=job_exp.job_title,
                company_name=job_exp.company_name,
                start_date=job_exp.start_date,
                end_date=job_exp.end_date,
                is_present_job=job_exp.is_present_job,
                description=job_exp.description
            )
            self.db.add(db_job_exp)
    
    def _create_skills(self, uuid_id: UUID, skills: list) -> None:
        """Create skill records."""
        for skill in skills:
            db_skill = SkillModel(
                form_data_id=uuid_id,
                name=skill.name,
                level=get_enum_value(skill.level) if skill.level else None,
                category=skill.category
            )
            self.db.add(db_skill)
    
    def _create_certifications(self, uuid_id: UUID, certifications: list) -> None:
        """Create certification records."""
        for cert in certifications:
            db_cert = CertificationModel(
                form_data_id=uuid_id,
                name=cert.name,
                issuer=cert.issuer,
                date_obtained=cert.date_obtained,
                expiry_date=cert.expiry_date,
                has_expiry=cert.has_expiry
            )
            self.db.add(db_cert)
    
    def _create_languages(self, uuid_id: UUID, languages: list) -> None:
        """Create language records."""
        for lang in languages:
            db_lang = LanguageModel(
                form_data_id=uuid_id,
                name=lang.name,
                proficiency=get_enum_value(lang.proficiency) if lang.proficiency else None
            )
            self.db.add(db_lang)
    
    def _create_projects(self, uuid_id: UUID, projects: list) -> None:
        """Create project records."""
        for project in projects:
            db_project = ProjectModel(
                form_data_id=uuid_id,
                title=project.title,
                description=project.description,
                technologies=project.technologies,
                link=project.link,
                start_date=project.start_date,
                end_date=project.end_date,
                is_ongoing=project.is_ongoing
            )
            self.db.add(db_project)

    def _create_references(self, uuid_id: UUID, references: list) -> None:
        """Create reference records."""
        for ref in references:
            db_ref = ReferenceModel(
                form_data_id=uuid_id,
                name=ref.name,
                position=ref.position,
                company=ref.company,
                email=ref.email,
                phone=ref.phone
            )
            self.db.add(db_ref)
