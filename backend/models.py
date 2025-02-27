from pydantic import BaseModel

class SurveyResponse(BaseModel):
    name: str
    gender: str
    nationality: str
    email: str
    phone_number: str
    address: str
    message: str
