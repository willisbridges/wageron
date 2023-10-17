from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import User, UserCreate, UserBase
from passlib.context import CryptContext

router = APIRouter()

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user
    """
    # Here is registration logic such as create new user in db
    existing_user = db.query(User).filter(
        (user.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="username or email already registered")

    # Hash the password before storing it in the database
    hashed_password = pwd_context.hash(user.password)
    db_user = User(**user.dict(), password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}/", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    """
    Get user info by user ID / get_current_user needs definition
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}/", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    """
    get user info by user ID
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # check if updated username/email is unique
    if (
            (user.username != existing_user.username and db.query(User).filter(User.username == user.username).first())
            or (user.email != existing_user.email and db.query(User).filter(User.email == user.email).first())
    ):
        raise HTTPException(status_code=400, detail="Username/Email already in use")

    # Update User data
    for key, value in user.dict().items():
        setattr(existing_user, key, value)
    db.commit()
    db.refresh(existing_user)
    return existing_user

# Add more user-related routes here
