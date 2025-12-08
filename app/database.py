from sqlmodel import SQLModel, create_engine, Session
from app.config import settings

# SQLite specific configuration
if "sqlite" in settings.database_url:
    engine = create_engine(settings.database_url, echo=True, connect_args={"check_same_thread": False})
else:
    engine = create_engine(settings.database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
