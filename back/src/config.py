from pydantic_settings import BaseSettings, SettingsConfigDict

class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    ) 
    MYSQL_USER: str 
    MYSQL_PASSWORD: str 
    MYSQL_DATABASE: str
    MYSQL_PORT: str
    MYSQL_ADDRESS: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    RUN_MODE: str = 'debug'
    DB: DBSettings = DBSettings()

settings = Settings()

