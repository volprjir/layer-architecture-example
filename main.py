from fastapi import FastAPI
from api import endpoints
from database import Base, engine

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)
app.include_router(endpoints.router)