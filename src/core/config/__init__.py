from pydantic_settings import BaseSettings, SettingsConfigDict

from .google import GoogleService


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env",),
        env_ignore_empty=True,
        extra="ignore",
        env_nested_delimiter="__",
    )

    TELEGRAM_TOKEN: str

    GOOGLE_SERVICE: GoogleService


settings = Settings()
