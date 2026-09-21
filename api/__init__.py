from fastapi import APIRouter
from . import echo, hello


def register_routers(app):
    """Registers all the API routers to the app"""
    router = APIRouter()

    router.include_router(echo.router, tags=["Echo"])
    router.include_router(hello.router, tags=["Hello"])

    app.include_router(router)