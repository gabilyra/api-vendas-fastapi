from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"), nullable=False)
    data_venda = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False, default=0)

    # Relacionamentos
    cliente = relationship("Cliente", back_populates="vendas")
    funcionario = relationship("Funcionario", back_populates="vendas")
    itens = relationship("ItemVenda", back_populates="venda")