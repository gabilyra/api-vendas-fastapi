from pydantic import BaseModel
from typing import Optional


class EnderecoBase(BaseModel):
    rua: str
    cidade: str
    estado: str


class EnderecoCreate(EnderecoBase):
    cliente_id: int


class EnderecoResponse(EnderecoBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True