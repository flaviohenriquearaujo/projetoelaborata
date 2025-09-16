
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Cliente_Data
# from models import Pedido_Data, Item_Pedido_Data, Insumos_Data, Status_Data
from schemas import Cliente

def criar_cliente(cliente: Cliente, db: Session):
    cliente_data = Cliente_Data(nome = cliente.nome, telefone= cliente.telefone, endereco = cliente.endereco,
                                status_id = cliente.status.id)

    db.add(cliente_data)
    db.commit()
    db.refresh(cliente_data)

    return cliente_data

def obter_cliente_por_nome(nome: str, db: Session):
    cliente  =db.query(Cliente_Data).filter(Cliente_Data.nome.ilike(f"%{nome}%")).all()
    return cliente

def obter_cliente(id: int, db: Session):
    cliente = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail=f"Cliente não encontrado!")
    
    return cliente

def alterar_cliente(id: int, cliente: Cliente, db: Session):
    cliente_data = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()

    if not cliente_data:
        raise HTTPException(status_code=404, detail=f"Cliente não encontrado!")
    
    cliente_data.nome = cliente.nome
    cliente_data.telefone = cliente.telefone
    cliente_data.endereco = cliente.endereco
    cliente_data.status_id = cliente.status.id

    db.commit()
    db.refresh(cliente_data)

    return cliente_data

def excluir_cliente(id: int, db: Session):

    cliente_data = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()

    if not cliente_data:
        raise HTTPException(status_code=404, detail=f"Cliente não encontrado!")
    
    db.delete(cliente_data)
    db.commit()
    
    return {"Mensagem": "Cliente excluído com sucesso"}

