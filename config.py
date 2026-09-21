from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # make sure environment variables match variables here
    # or use 'validation_alias' 

    app_name: str = "refund_agent"
    debug: bool =  False
    environment: str = "development"
    version: str = "0.0.1"

