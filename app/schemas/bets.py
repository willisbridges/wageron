from pydantic import BaseModel
from typing import Optional


class BetBase(BaseModel):
    description: str
    amount: float


class BetCreate(BetBase):
    pass


class BetUpdate(BaseModel):
    description: Optional[str] = None
    amount: Optional[float] = None


class BetInDB(BetBase):
    id: int
    user_id: int


class Bet(BetInDB):
    pass
