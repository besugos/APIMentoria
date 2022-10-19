from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from persistency.employee_persistency import EmployeePersistency
from models.models import Employee, User
from persistency.persistency_utils import get_db, create_db
from utils.authentication_utils import verify_hash, get_user_info, create_token

create_db()

router = APIRouter(
    prefix="/employees",
    tags=["Employee"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_employees(db: Session = Depends(get_db), user=Depends(get_user_info)):
    employees = EmployeePersistency(db).read()
    return employees


@router.get("/{employee_id}")
async def get_employee_by_id(employee_id: int,  db: Session = Depends(get_db)):
    employee = EmployeePersistency(db).read_by_id(employee_id)
    return employee


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_employee(employee: Employee, db: Session = Depends(get_db), user=Depends(get_user_info)):
    created_employee = EmployeePersistency(db).create(employee)
    return created_employee


@router.delete("/{employee_id}")
async def get_employee_by_id(employee_id: int,  db: Session = Depends(get_db)):
    employee = EmployeePersistency(db).delete(employee_id)
    return {"msg": "Deleted successfully"}


@router.patch("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def edit_employee(employee: Employee, employee_id: int, db: Session = Depends(get_db)):
    EmployeePersistency(db).patch(employee, employee_id)
    return {"msg": "Edit successfully"}


@router.post("/login")
async def login(login_data: User, db: Session = Depends(get_db)):
    password = login_data.password
    username = login_data.email
    user = EmployeePersistency(db).read_by_username(username)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong credentials')

    valid_password = verify_hash(password, user.password)

    if not valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong credentials')

    token = create_token({'sub': user.email})

    return {"user": user, "token": token['token']}

