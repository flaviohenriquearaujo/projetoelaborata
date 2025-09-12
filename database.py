from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



SQLALCHEMY_DATABASE_URL = "sqlite:///./projeto_flavio.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #representa uma conexão com um banco de dados SQLite

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close