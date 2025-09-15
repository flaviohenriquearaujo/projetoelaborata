
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Insumos_Data
from schemas import Insumos

def criar_insumo(insumo: Insumos, db: Session):
    insumo_data = Insumos_Data(nome = insumo.nome,
                               quantidade = insumo.quantidade, 
                               custo_unitario = insumo.custo_unitario,
                               custo_total = insumo.custo_total,
                               pedido_id = insumo.pedido.id,
                               produto_id = insumo.produto.id
                               )

    db.add(insumo_data)
    db.commit()
    db.refresh(insumo_data)

    return insumo_data

def obter_insumo_por_nome(nome: str, db: Session):
    insumo  =db.query(Insumos_Data).filter(Insumos_Data.nome.ilike(f"%{nome}%")).all()
    return insumo

def obter_insumo(id: int, db: Session):
    insumo = db.query(Insumos_Data).filter(Insumos_Data.id == id).first()

    if not insumo:
        raise HTTPException(status_code=404, detail=f"insumo não encontrado!")
    
    return insumo

def alterar_insumo(id: int, insumo: Insumos, db: Session):
    insumo_data = db.query(Insumos_Data).filter(Insumos_Data.id == id).first()

    if not insumo_data:
        raise HTTPException(status_code=404, detail=f"insumo não encontrado!")
    
    insumo_data.nome = insumo.nome
    insumo_data.quantidade = insumo.quantidade
    insumo_data.custo_unitario = insumo.custo_unitario
    insumo_data.custo_total = insumo.custo_total
    insumo_data.pedido_id = insumo.pedido.id
    insumo_data.produto_id = insumo.produto.id

    db.commit()
    db.refresh(insumo_data)

    return insumo_data

def excluir_insumo (id: int, db: Session):

    insumo_data = db.query(Insumos_Data).filter(Insumos_Data.id == id).first()

    if not insumo_data:
        raise HTTPException(status_code=404, detail=f"insumo não encontrado!")
    
    db.delete(insumo_data)
    db.commit()
    
    return {"Mensagem": "insumo excluído com sucesso"}

