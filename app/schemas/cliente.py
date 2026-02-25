from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None


class ClienteResponse(ClienteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True