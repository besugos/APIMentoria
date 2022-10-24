from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from persistency.dayoff_persistency import DayoffPersistency
from models.models import Dayoff
from persistency.persistency_utils import get_db, create_db
from utils.authentication_utils import get_user_info


router = APIRouter(
    prefix="/dayoffs",
    tags=["Dayoff"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_dayoffs(db: Session = Depends(get_db), user=Depends(get_user_info)):
    dayoffs = DayoffPersistency(db).read()
    return dayoffs


@router.get("/{dayoff_id}")
async def get_dayoff_by_id(dayoff_id: int,  db: Session = Depends(get_db)):
    dayoff = DayoffPersistency(db).read_by_id(dayoff_id)
    return dayoff


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_dayoff(dayoff: Dayoff, db: Session = Depends(get_db), user=Depends(get_user_info)):
    created_dayoff = DayoffPersistency(db).create(dayoff)
    return created_dayoff


@router.delete("/{dayoff_id}")
async def delete_dayoff(dayoff_id: int,  db: Session = Depends(get_db)):
    dayoff = DayoffPersistency(db).delete(dayoff_id)
    return {"msg": "Deleted successfully"}


@router.patch("/{dayoff_id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit_dayoff(dayoff: Dayoff, dayoff_id: int, db: Session = Depends(get_db), user=Depends(get_user_info)):
    DayoffPersistency(db).patch(dayoff, dayoff_id)
    return {"msg": "Edit successfully"}

