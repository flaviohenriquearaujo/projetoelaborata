
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import date
from models import Pedido_Data
from routers import cliente
from schemas import Pedido

def criar_pedido(pedido: Pedido, db: Session):
    pedido_data = Pedido_Data(data_pedido = pedido.data_pedido,
                              data_entrega = pedido.data_entrega,
                              tipo_entrega = pedido.tipo_entrega,
                              observacoes = pedido.observacoes,
                              cliente_id = pedido.cliente.id,
                              status_id = pedido.status.id
                              )

    db.add(pedido_data)
    db.commit()
    db.refresh(pedido_data)

    return pedido_data






def obter_pedido_por_nome_cliente(cliente_id: int, db: Session):
    # cliente = db.query(Cliente).filter(Cliente.nome == nome_cliente).first()
                
    pedido = db.query(Pedido_Data).filter(Pedido_Data.cliente_id == cliente.id).all
    
    if not pedido:
        raise HTTPException(status_code=404, detail=f"pedido não encontrado!")
    
    
    # pedido  =db.query(Pedido_Data).filter(Pedido_Data.nome.ilike(f"%{nome}%")).all()
    
    return pedido




def obter_pedido(id_nr_pedido: int, db: Session):
    pedido = db.query(Pedido_Data).filter(Pedido_Data.id_nr_pedido == id_nr_pedido).first()

    if not pedido:
        raise HTTPException(status_code=404, detail=f"pedido não encontrado!")
    
    return pedido

def alterar_pedido(id_nr_pedido: int, pedido: Pedido, db: Session):
    pedido_data = db.query(Pedido_Data).filter(Pedido_Data.id_nr_pedido == id_nr_pedido).first()

    if not pedido_data:
        raise HTTPException(status_code=404, detail=f"pedido não encontrado!")
    
    pedido_data.data_pedido = pedido.data_pedido
    pedido_data.data_entrega = pedido.data_entrega,
    pedido_data.tipo_entrega = pedido.tipo_entrega,
    pedido_data.observacoes = pedido.observacoes,
    pedido_data.cliente_id = pedido.cliente.id,
    pedido_data.status_id = pedido.status.id
 
    db.commit()
    db.refresh(pedido_data)

    return pedido_data

def excluir_pedido(id_nr_pedido: int, db: Session):

    pedido_data = db.query(Pedido_Data).filter(Pedido_Data.id_nr_pedido == id_nr_pedido).first()

    if not pedido_data:
        raise HTTPException(status_code=404, detail=f"pedido não encontrado!")
    
    db.delete(pedido_data)
    db.commit()
    
    return {"Mensagem": "pedido excluído com sucesso"}

