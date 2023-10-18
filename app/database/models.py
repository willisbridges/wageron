from pydantic import BaseModel


class UserBase(BaseModel):
    """
    base Pydantic model for user data
    """
    username: str
    email: str


class UserCreate(UserBase):
    """
    Pydantic model for user data during user registration
    """
    password: str


class User(UserBase):
    """
    Pydantic model for returning user data in API responses
    """
    id: int

    class Config:
        orm_mode = True


class BetBase(BaseModel):
    """
    base Pydantic model for bet data
    """
    description: str
    wager_amount: float
    outcome: str


class BetCreate(BetBase):
    """
    Pydantic mode for creating new bets
    """
    pass


class Bet(BetBase):
    """
    Pydantic model for returning bet data in API responses
    """
    id: int
    is_resolved: bool
    owner_id: int
    winner_id: int = None  # Winner's user ID when the bet is resolved

    class Config:
        orm_mode = True


class BetUpdate(BaseModel):
    """
    Pydantic model for updating bet data
    """
    is_resolved: bool
    winner_id: int  # Winner's user ID when bet is resolved


class BetResolve(BaseModel):
    """
    Pydantic model for resolving bets based on CoD API criteria.
    """
    resolved_by: str  # will need to explore the CoD API and see how to resolve bets / what data types
