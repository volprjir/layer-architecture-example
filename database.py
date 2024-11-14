from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config.constants import SQLALCHEMY_DATABASE_URL, ASYNC_SQLALCHEMY_DATABASE_URL


SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the asynchronous session
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)