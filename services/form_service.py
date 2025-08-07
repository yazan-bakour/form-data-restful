from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from models.schemas import FormData
from models.response_schemas import FormDataResponse
from services.repositories.form_data_repository import FormDataRepository
from services.mappers.form_data_mapper import FormDataMapper

class FormService:
    def __init__(self, db: Session):
        """Initialize service with dependencies."""
        self.repository = FormDataRepository(db)
        self.mapper = FormDataMapper()
    
    def create_form_data(self, form_data: FormData) -> FormDataResponse:
        """Create a new form data entry."""
        db_form_data = self.repository.create(form_data)
        return self.mapper.db_to_response_model(db_form_data)
    
    def get_form_data(self, form_id: str) -> Optional[FormDataResponse]:
        """Retrieve form data by ID."""
        db_form_data = self.repository.get_by_id(form_id)
        if not db_form_data:
            return None
        return self.mapper.db_to_response_model(db_form_data)
    
    def get_all_form_data(self) -> List[FormDataResponse]:
        """Retrieve all form data entries."""
        db_list = self.repository.get_all()
        return self.mapper.db_list_to_response_list(db_list)
    
    def update_form_data(self, form_id: str, form_data: FormData) -> Optional[FormDataResponse]:
        """Update existing form data."""
        db_form_data = self.repository.update(form_id, form_data)
        if not db_form_data:
            return None
        return self.mapper.db_to_response_model(db_form_data)
    
    def delete_form_data(self, form_id: str) -> Optional[FormDataResponse]:
        """Delete form data by ID."""
        db_form_data = self.repository.delete(form_id)
        if not db_form_data:
            return None
        return self.mapper.db_to_response_model(db_form_data)
    
    def search_form_data(self, first_name: Optional[str] = None, last_name: Optional[str] = None,
                        email: Optional[str] = None, job_title: Optional[str] = None) -> List[FormDataResponse]:
        """Search form data based on criteria."""
        db_results = self.repository.search(first_name, last_name, email, job_title)
        return self.mapper.db_list_to_response_list(db_results)
    
    def get_storage_info(self) -> Dict[str, Any]:
        """Get storage information."""
        total_entries = self.repository.count()
        return {
            "total_entries": total_entries,
            "storage_type": "database",
            "database_engine": "postgresql/sqlite"
        }