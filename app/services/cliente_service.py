from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate
from typing import Optional, List
from fastapi import HTTPException


def criar_cliente(db: Session, cliente_data: ClienteCreate):
    novo_cliente = Cliente(**cliente_data.model_dump())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


def listar_clientes(
    db: Session,
    nome: Optional[str] = None,
    email: Optional[str] = None
):
    query = db.query(Cliente)

    if nome:
        query = query.filter(Cliente.nome.ilike(f"%{nome}%"))

    if email:
        query = query.filter(Cliente.email.ilike(f"%{email}%"))

    return query.all()


def buscar_cliente_por_id(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return cliente


def atualizar_cliente(db: Session, cliente_id: int, cliente_data):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    for key, value in cliente_data.model_dump(exclude_unset=True).items():
        setattr(cliente, key, value)

    db.commit()
    db.refresh(cliente)

    return cliente


def deletar_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(cliente)
    db.commit()

    return {"message": "Cliente deletado com sucesso"}