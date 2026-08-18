from database.connection import engine
from sqlalchemy.orm import Session, sessionmaker

SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    autoflush=False,
    expire_on_commit=False,
)