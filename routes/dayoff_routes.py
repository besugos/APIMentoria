from fastapi import APIRouter

router = APIRouter(
    prefix="/dayoff",
    tags=["Dayoff"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_dayoffs():
    return {"msg": "get all dayoffs route"}


@router.get("/{id}")
async def get_dayoff_by_id():
    return {"msg": "get dayoff by id route"}
