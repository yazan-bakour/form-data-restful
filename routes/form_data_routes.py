from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional, List, Dict, Union
from sqlalchemy.orm import Session
from models.schemas import FormData
from models.response_schemas import ApiResponse, FormDataResponse, CreateResponse, StorageInfoResponse
from services import FormService
from database.connection import get_db
from utils.response_helpers import (
    success_response, 
    created_response, 
    storage_info_response, 
    error_response,
    NOT_FOUND_MESSAGE
)

router = APIRouter(prefix="/api/v1/form-data", tags=["Form Data"])

@router.post("/", response_model=ApiResponse[CreateResponse])
async def create_form_data(form_data: FormData, db: Session = Depends(get_db)):
    try:
        form_service = FormService(db)
        result = form_service.create_form_data(form_data)
        return created_response(result.id)
    except Exception as e:
        return error_response({"detail": str(e)}, "Error creating form data", 500)


@router.get("/search", response_model=ApiResponse[List[FormDataResponse]])
async def search_form_data(
    db: Session = Depends(get_db),
    first_name: Optional[str] = Query(None, description="First name to search for"),
    last_name: Optional[str] = Query(None, description="Last name to search for"),
    email: Optional[str] = Query(None, description="Email to search for"),
    job_title: Optional[str] = Query(None, description="Job title to search for")
):
    try:
        form_service = FormService(db)
        result = form_service.search_form_data(
            first_name=first_name,
            last_name=last_name,
            email=email,
            job_title=job_title
        )
        return success_response(result, "Search successful")
    except Exception as e:
        return error_response({"detail": str(e)}, "Error searching form data", 500)


@router.get("/{form_id}", response_model=ApiResponse[FormDataResponse])
async def get_form_data(form_id: str, db: Session = Depends(get_db)):
    form_service = FormService(db)
    result = form_service.get_form_data(form_id)
    if result is None:
        return error_response({"id": f"Form data with ID {form_id} not found"}, NOT_FOUND_MESSAGE, 404)
    return success_response(result, "Fetch successful")


@router.get("/", response_model=ApiResponse[List[FormDataResponse]])
async def get_all_form_data(db: Session = Depends(get_db)):
    try:
        form_service = FormService(db)
        result = form_service.get_all_form_data()
        return success_response(result, "Fetch all successful")
    except Exception as e:
        return error_response({"detail": str(e)}, "Error retrieving form data", 500)


@router.put("/{form_id}", response_model=ApiResponse[FormDataResponse])
async def update_form_data(form_id: str, form_data: FormData, db: Session = Depends(get_db)):
    form_service = FormService(db)
    result = form_service.update_form_data(form_id, form_data)
    if result is None:
        return error_response({"id": f"Form data with ID {form_id} not found"}, NOT_FOUND_MESSAGE, 404)
    return success_response(result, "Update successful")


@router.delete("/{form_id}", response_model=ApiResponse[FormDataResponse])
async def delete_form_data(form_id: str, db: Session = Depends(get_db)):
    form_service = FormService(db)
    result = form_service.delete_form_data(form_id)
    if result is None:
        return error_response({"id": f"Form data with ID {form_id} not found"}, NOT_FOUND_MESSAGE, 404)
    return success_response(result, "Delete successful")


@router.get("/storage/info", response_model=ApiResponse[StorageInfoResponse])
async def get_storage_info(db: Session = Depends(get_db)):
    try:
        form_service = FormService(db)
        result = form_service.get_storage_info()
        return storage_info_response(result)
    except Exception as e:
        return error_response({"detail": str(e)}, "Error getting storage info", 500)
