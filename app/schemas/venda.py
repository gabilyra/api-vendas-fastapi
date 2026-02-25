from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal


class VendaBase(BaseModel):
    cliente_id: int
    funcionario_id: int


class VendaCreate(VendaBase):
    pass


class VendaResponse(VendaBase):
    id: int
    data_venda: datetime
    valor_total: Decimal

    class Config:
        from_attributes = True