from pydantic import BaseModel
from decimal import Decimal


class ProdutoBase(BaseModel):
    nome: str
    preco: Decimal
    estoque: int


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True