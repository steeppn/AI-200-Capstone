from fastapi import FastAPI
from api import register_routers
from config import Settings

from contextlib import asynccontextmanager

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    "Handles startup and shutdown events"
    print ('Refund agent has started...')
    yield
    print ('Refund agent shutting down...')

def create_app() -> FastAPI:

    app = FastAPI(
        title = settings.app_name,
        description = 'Agent for handling refunds',
        version = settings.version,
        debug = settings.debug,
        lifespan = lifespan,
    )
    register_routers(app)
    return app


app = create_app()


