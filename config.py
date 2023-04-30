from pydantic import BaseSettings

class Settings(BaseSettings):
    PORT : int
    DB_NAME: str
    MONGODB_URI : str
    BEARER: str

    class Config:
        env_file = '.env'

config = Settings()

