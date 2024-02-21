import uvicorn
from fastapi import FastAPI, APIRouter
from app.config import db

# app = FastAPI()

# router = APIRouter()

# @router.get("/")

# async def home():
#     return"welcome home"

# app.include_router(router)

def init_app():
    db.init()

    app = FastAPI(
        title="Backend Projesi",
        description="LoginPage",
        version="0.1.0"
    )
    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    return app

app = init_app()

def start():
    """Launched wih 'poetry run start' at root level"""
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)