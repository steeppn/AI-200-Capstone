from typing import Literal

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.local", 
        extra="ignore",
        )

    # make sure environment variables match variables here
    # or use 'validation_alias' 

    AZURE_LLM_ENDPOINT: str = ""
    LLM_MODEL_NAME: str = ""

    LLM_BACKEND: Literal["mock", "azure"] = "azure"

    database_url: str | None = None
    redis_url: str | None = None
    
    app_name: str = "refund_agent"
    debug: bool =  False
    environment: Literal["local", "production"] = "production"
    version: str = "0.0.1"

    @model_validator(mode="after")
    def validate_backend(self):
        if (
            self.environment == "production"
            and self.LLM_BACKEND != "azure"
        ):
            raise ValueError(
                "Production requires Azure backend"
            )
        if (
            self.LLM_BACKEND == "azure"
            and self.environment == "production"
            and (
                not self.AZURE_LLM_ENDPOINT
                or not self.LLM_MODEL_NAME
            )
        ):
            raise ValueError(
                "Production requires Azure endpoint "
                "and model deployment name"
            )
        return self
    

