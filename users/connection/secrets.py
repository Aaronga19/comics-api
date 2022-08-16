import os
from pydantic import BaseSettings

# Settings
class Settings(BaseSettings):
    database_hostname: str
    database_password: str
    database_name: str
    database_username: str
    database_collection: str
    secret_key: str  
    algorithm: str
    access_token_expires_minutes: int
    api_key: str
    api_key_name: str
    cookie_domain: str

    class Config:
        env_file = "connection/.env"
settings = Settings()