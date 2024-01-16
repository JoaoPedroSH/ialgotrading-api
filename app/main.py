from functools import lru_cache
from fastapi import Depends, FastAPI
from typing_extensions import Annotated
from .routers import items, users

from .configs.config import Settings

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@lru_cache
def get_settings():
    return Settings()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }