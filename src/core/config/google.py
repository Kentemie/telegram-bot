from pydantic import BaseModel, field_validator


class BaseService(BaseModel):
    SCOPES: list[str] | str

    @field_validator("SCOPES", mode="after")  # noqa
    @classmethod
    def _check_scopes_type(cls, value: list[str] | str) -> list[str]:
        if isinstance(value, str):
            value = [value]

        return value


class Sheets(BaseService): ...  # noqa


class Drive(BaseService): ...  # noqa


class GoogleService(BaseModel):
    SHEETS: Sheets
    DRIVE: Drive

    KEY_PATH: str
