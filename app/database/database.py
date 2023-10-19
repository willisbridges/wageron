from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./test.db"  # Replace with Database URL

# Create engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class for handling database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base object for declarative models
Base = declarative_base()
