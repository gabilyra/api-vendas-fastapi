from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteResponse, ClienteUpdate
from app.services import cliente_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# Criar cliente
@router.post("/", response_model=ClienteResponse)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.criar_cliente(db, cliente)

# Listar clientes
@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(
    nome: Optional[str] = None,
    email: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return cliente_service.listar_clientes(db, nome, email)

# Buscar cliente
@router.get("/{cliente_id}", response_model=ClienteResponse)
def buscar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return cliente_service.buscar_cliente_por_id(db, cliente_id)

# Atualizar cliente
@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(
    cliente_id: int,
    cliente_data: ClienteUpdate,
    db: Session = Depends(get_db)
):
    return cliente_service.atualizar_cliente(db, cliente_id, cliente_data)

# Deletar cliente
@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return cliente_service.deletar_cliente(db, cliente_id)