from pydantic import BaseSettings

class Settings(BaseSettings):
    PORT : int
    MONGODB_URI : str

    class Config:
        env_file = '.env'

config = Settings()

