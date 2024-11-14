from config.celery_app import celery_app


@celery_app.task
async def send_sms(phone):
    print(f"Sending SMS to {phone}.")


@celery_app.task
async def send_email(email: str):
    print(f"Sending registration confirmation email to {email}")
