from fastapi import FastAPI
from app.users.routes import router as users_router

app = FastAPI(title="Учебный проект")

app.include_router(users_router, prefix="/users", tags=["Users"])