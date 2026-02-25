from pydantic import BaseModel
from decimal import Decimal


class FuncionarioBase(BaseModel):
    nome: str
    cargo: str
    salario: Decimal


class FuncionarioCreate(FuncionarioBase):
    pass


class FuncionarioResponse(FuncionarioBase):
    id: int

    class Config:
        from_attributes = True