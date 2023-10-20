from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    id: int


class User(UserInDB):
    pass
