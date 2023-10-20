from pydantic import BaseModel


class BetBase(BaseModel):
    description: str
    amount: float


class BetCreate(BetBase):
    pass


class BetInDB(BetBase):
    id: int
    user_id: int


class Bet(BetInDB):
    pass
