from fastapi import APIRouter, Depends, HTTPException
from superagi.helper.auth import check_auth, get_user_organisation
from superagi.helper.models_helper import ModelsHelper
from fastapi_jwt_auth import AuthJWT
from fastapi_sqlalchemy import db
import logging
from pydantic import BaseModel

router = APIRouter()

class ValidateAPIKeyRequest(BaseModel):
    model_provider: str
    model_api_key: str

class StoreModelRequest(BaseModel):
    model_name: str
    description: str
    end_point: str
    model_provider_id: int
    token_limit: int

@router.post("/storeApiKeys")
async def storeApiKeys(request: ValidateAPIKeyRequest, organisation=Depends(get_user_organisation)):
    try:
        return ModelsHelper(session=db.session, organisation_id=organisation.id).storeApiKey(request.model_provider, request.model_api_key)
    except Exception as e:
        logging.error(f"Error while storing API key: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/getApiKeys")
async def getApiKeys(organisation=Depends(get_user_organisation)):
    try:
        return ModelsHelper(session=db.session, organisation_id=organisation.id).fetchApiKeys()
    except Exception as e:
        logging.error(f"Error while retrieving API Keys: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/getApiKey")
async def getApiKey(model_provider: str = None, organisation=Depends(get_user_organisation)):
    try:
        return ModelsHelper(session=db.session, organisation_id=organisation.id).fetchApiKey(model_provider)
    except Exception as e:
        logging.error(f"Error while retrieving API Key: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/verifyEndPoint")
async def verifyEndPoint(model_api_key: str = None, end_point: str = None, organisation=Depends(get_user_organisation)):
    try:
        return ModelsHelper(session=db.session, organisation_id=organisation.id).validateEndPoint(model_api_key, end_point)
    except Exception as e:
        logging.error(f"Error validating Endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/storeModel")
async def storeModel(request: StoreModelRequest, organisation=Depends(get_user_organisation)):
    try:
        return ModelsHelper(session=db.session, organisation_id=organisation.id).storeModelDetails(request.model_name, request.description, request.end_point, request.model_provider_id, request.token_limit)
    except Exception as e:
        logging.error(f"Error storing the Model Details: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/fetchModels")
async def fetchModels(organisation=Depends(get_user_organisation)):
    try:
        return ModelsHelper(session=db.session, organisation_id=organisation.id).fetchModels()
    except Exception as e:
        logging.error(f"Error Fetching Models: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")