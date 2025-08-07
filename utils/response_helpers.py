from typing import Optional, List, Union, Dict
from fastapi.responses import JSONResponse
from models.response_schemas import FormDataResponse, CreateResponse, StorageInfoResponse

NOT_FOUND_MESSAGE = "Not found"

def success_response(data: Optional[Union[FormDataResponse, List[FormDataResponse]]] = None, message: str = ""):
    payload = {"success": True, "message": message}
    if data is not None:
        if isinstance(data, list):
            payload["data"] = [item.model_dump() for item in data]
        else:
            payload["data"] = data.model_dump()
    return JSONResponse(status_code=200, content=payload)

def created_response(form_id: str, message: str = "Form data created"):
    create_data = CreateResponse(id=form_id)
    payload = {"success": True, "message": message, "data": create_data.model_dump()}
    return JSONResponse(status_code=201, content=payload)

def storage_info_response(storage_data: Dict[str, str | int], message: str = "Storage info fetched"):
    storage_model = StorageInfoResponse(**storage_data)
    payload = {"success": True, "message": message, "data": storage_model.model_dump()}
    return JSONResponse(status_code=200, content=payload)

def error_response(errors: Dict[str, str], message: str, status_code: int = 400):
    payload = {"success": False, "message": message, "errors": errors}
    return JSONResponse(status_code=status_code, content=payload)
