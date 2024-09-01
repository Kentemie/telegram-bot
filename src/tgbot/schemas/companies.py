from pydantic import BaseModel


class Sheet(BaseModel):
    id: int
    sheet_id: str
    sheet_name: str


class Company(BaseModel):
    id: int
    name: str
