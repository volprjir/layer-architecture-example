from services.messaging_service import send_email, send_sms
from services.registration_service import register_user_task
from models.schemas import UserCreate

async def register_user(user: UserCreate):
    task = register_user_task.delay(user)
    send_email.delay(user.email)
    send_sms.delay(user.phone)
    return task.id

async def import_user(user: UserCreate):
    task = register_user_task.delay(user)
    send_email.delay(user.email)
    return task.id