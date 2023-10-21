from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.bets import Bet, BetCreate, BetUpdate

router = APIRouter()


@router.post("/bets/", response_model=Bet)
def create_bet(bet: BetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Create a new bet
    """
    db_bet = Bet(**bet.dict(), user_id=current_user.id)
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet


@router.get("/bets/{bet_id}", response_model=Bet)
def read_bet(bet_id: int, db: Session = Depends(get_db)):
    """
    Get info for Bet ID
    """
    # TODO: Retrieve bet from database HERE
    # return updated bet
    return {"bet_id": bet_id, "updated_details": "updated bet details HERE"}


@router.delete("/bets/{bet_id}", response_model=Bet)
def delete_bet(bet_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific bet by ID
    """
    # TODO: Delete bet from database HERE
    # return deleted bet
    return {"bet_id": bet_id, "status": "deleted"}
