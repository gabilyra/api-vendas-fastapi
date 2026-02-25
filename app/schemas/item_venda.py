from pydantic import BaseModel
from decimal import Decimal


class ItemVendaBase(BaseModel):
    venda_id: int
    produto_id: int
    quantidade: int
    preco_unitario: Decimal


class ItemVendaCreate(ItemVendaBase):
    pass


class ItemVendaResponse(ItemVendaBase):
    id: int

    class Config:
        from_attributes = True