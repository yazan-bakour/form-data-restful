"""
Data mapping layer for converting between database models and response models.
Handles all model transformation logic.
"""
from typing import List
from models.response_schemas import (
    FormDataResponse, EducationResponse, JobExperienceResponse, SkillResponse,
    CertificationResponse, LanguageResponse, ProjectResponse, ReferenceResponse
)
from database.models import FormDataModel


class FormDataMapper:
    """
    Mapper class responsible for converting database models to response models.
    Follows the Data Mapper pattern for clean separation of concerns.
    """

    @staticmethod
    def db_to_response_model(db_form_data: FormDataModel) -> FormDataResponse:
        """Convert database model to Pydantic response model."""
        educations = [EducationResponse(
            id=str(edu.id),
            university_name=edu.university_name,
            degree_type=edu.degree_type,
            course_name=edu.course_name
        ) for edu in db_form_data.educations]
        
        job_experiences = [JobExperienceResponse(
            id=str(job.id),
            job_title=job.job_title,
            company_name=job.company_name,
            start_date=job.start_date,
            end_date=job.end_date,
            is_present_job=job.is_present_job,
            description=job.description
        ) for job in db_form_data.job_experiences]
        
        skills = [SkillResponse(
            id=str(skill.id),
            name=skill.name,
            level=skill.level,
            category=skill.category
        ) for skill in db_form_data.skills]
        
        certifications = [CertificationResponse(
            id=str(cert.id),
            name=cert.name,
            issuer=cert.issuer,
            date_obtained=cert.date_obtained,
            expiry_date=cert.expiry_date,
            has_expiry=cert.has_expiry
        ) for cert in db_form_data.certifications]
        
        languages = [LanguageResponse(
            id=str(lang.id),
            name=lang.name,
            proficiency=lang.proficiency
        ) for lang in db_form_data.languages]
        
        projects = [ProjectResponse(
            id=str(proj.id),
            title=proj.title,
            description=proj.description,
            technologies=proj.technologies,
            link=proj.link,
            start_date=proj.start_date,
            end_date=proj.end_date,
            is_ongoing=proj.is_ongoing
        ) for proj in db_form_data.projects]
        
        references = [ReferenceResponse(
            id=str(ref.id),
            name=ref.name,
            position=ref.position,
            company=ref.company,
            email=ref.email,
            phone=ref.phone
        ) for ref in db_form_data.references]
        
        return FormDataResponse(
            id=str(db_form_data.id),
            first_name=db_form_data.first_name,
            last_name=db_form_data.last_name,
            email=db_form_data.email,
            mobile_number=db_form_data.mobile_number,
            date_of_birth=db_form_data.date_of_birth,
            street_address=db_form_data.street_address,
            city=db_form_data.city,
            state=db_form_data.state,
            postal_code=db_form_data.postal_code,
            country=db_form_data.country,
            title=db_form_data.title,
            marital_status=db_form_data.marital_status,
            developer=db_form_data.developer,
            job=db_form_data.job,
            portfolio_website=db_form_data.portfolio_website,
            github_url=db_form_data.github_url,
            linkedin_url=db_form_data.linkedin_url,
            preferred_work_type=db_form_data.preferred_work_type,
            expected_salary=db_form_data.expected_salary,
            preferred_location=db_form_data.preferred_location,
            availability_date=db_form_data.availability_date,
            career_goals=db_form_data.career_goals,
            professional_summary=db_form_data.professional_summary,
            hobbies=db_form_data.hobbies,
            volunteer_work=db_form_data.volunteer_work,
            additional_notes=db_form_data.additional_notes,
            created_at=db_form_data.created_at.isoformat() if db_form_data.created_at else None,
            updated_at=db_form_data.updated_at.isoformat() if db_form_data.updated_at else None,
            educations=educations,
            job_experiences=job_experiences,
            skills=skills,
            certifications=certifications,
            languages=languages,
            projects=projects,
            references=references
        )
    
    @staticmethod
    def db_list_to_response_list(db_form_data_list: List[FormDataModel]) -> List[FormDataResponse]:
        """Convert list of database models to list of response models."""
        return [FormDataMapper.db_to_response_model(db_form_data) for db_form_data in db_form_data_list]
