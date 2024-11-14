from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    company_id: int