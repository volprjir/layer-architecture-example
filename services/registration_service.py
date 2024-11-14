from database import async_session
from config.celery_app import celery_app
from models.schemas import UserCreate
from repositories.user_repository import create_user

@celery_app.task
async def register_user_task(user: UserCreate):
    async with async_session() as db:
        db_user = await create_user(db, user)
        return db_user.id