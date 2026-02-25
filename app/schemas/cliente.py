from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteResponse(ClienteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True