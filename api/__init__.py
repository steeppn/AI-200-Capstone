from fastapi import APIRouter
from . import health, run


def register_routers(app):
    """Registers all the API routers to the app"""
    router = APIRouter()

    router.include_router(run.router, tags=["Run"])
    router.include_router(health.router, tags=["Health"])

    app.include_router(router)