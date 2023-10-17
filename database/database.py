from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Replace with Database URL

# Create engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class for handling database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    This function if used as a dependency to get a DB session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
