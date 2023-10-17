from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Bet, BetCreate, BetUpdate, BetResolve

router = APIRouter()


@router.post("/bets/", response_model=Bet)
def create_bet(bet: BetCreate, db: Session = Depends(get_db)):
    """
    endpoint for creating a new bet
    """
    # Bet creation logic goes here, create new bet in db?
    return bet
