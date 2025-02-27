from fastapi import APIRouter, HTTPException, Depends
from database import collection
from models import SurveyResponse
from typing import List

router = APIRouter()


@router.post("/submit")
async def submit_survey(response: SurveyResponse):
    # Check if phone number already exists in the database
    existing_user = collection.find_one({"phone_number": response.phone_number})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    # Insert new survey response
    collection.insert_one(response.dict())
    return {"message": "Survey submitted successfully!"}

@router.get("/responses")
async def get_responses(password: str):
    if password != "admin":
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    responses = list(collection.find({}, {"_id": 0}))  # Exclude `_id`
    
    # Rename `phone_number` to `phone` to match React frontend
    for response in responses:
        response["phone"] = response.pop("phone_number", "")
    
    return responses