import uvicorn
from fastapi import FastAPI, APIRouter
from routes import employee_routes, dayoff_routes

app = FastAPI()

router = APIRouter()
router.include_router(employee_routes.router)
router.include_router(dayoff_routes.router)

app.include_router(router)


@app.get("/")
async def root():
    return {"msg": "Hello World!"}


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
    print("running")



