from fastapi import FastAPI
from api import register_routers
from config import Settings
import yaml
import logging

from contextlib import asynccontextmanager

from openai import AsyncOpenAI
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider
from classes.refund_agent import Refund_Agent

settings = Settings()

logging.basicConfig(level=logging.INFO, format="%(levelname)s: [%(name)s] %(message)s")
logger = logging.getLogger("ai-agent")


@asynccontextmanager
async def lifespan(app: FastAPI):
    "Handles startup and shutdown events"
    logger.info("Container booting up...")

    with open ("llm_config.yaml", "r") as file:
        app.state.llm_config = yaml.safe_load(file)

    app.state._settings = settings
    app.state.openai_client = None
    app.state.refund_agent = None
    if settings.AZURE_LLM_ENDPOINT and settings.LLM_MODEL_NAME:
        logger.info("Initializing AsyncOpenAI client with provided configurations...")

        credential = DefaultAzureCredential()
        bearer_token = get_bearer_token_provider(credential, 'https://ai.azure.com/.default')

        app.state.openai_client = AsyncOpenAI(
            base_url=settings.AZURE_LLM_ENDPOINT,
            api_key=bearer_token,
        )

        app.state.credential = credential

        app.state.refund_agent = Refund_Agent(
            openai_client=app.state.openai_client,
            model_deployment_name=app.state._settings.LLM_MODEL_NAME,
            llm_config=app.state.llm_config,
        )
        logger.info("AsyncOpenAI client has been successfully initialized")
    else:
        logger.error("Upstream configuration missing, UNREADY")
    yield

    if getattr(app.state, "openai_client", None):
        await app.state.openai_client.close()
        await app.state.credential.close()

    logger.info("Container shut down.")

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


