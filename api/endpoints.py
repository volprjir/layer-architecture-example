from fastapi import APIRouter
from models.schemas import UserCreate
from services.user_service import register_user, import_user

router = APIRouter()

@router.post("/register/")
async def register_user_endpoint(user: UserCreate):
    task_id = await register_user(user)
    return {"message": "User registration in progress", "task_id": task_id}

@router.post("/import_user/")
async def import_user_endpoint(user: UserCreate):
    task_id = await import_user(user)
    return {"message": "User import in progress", "task_id": task_id}