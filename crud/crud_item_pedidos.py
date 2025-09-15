
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Item_Pedido_Data
from schemas import Item_Pedido

def criar_item_pedido(item_pedido: Item_Pedido, db: Session):
    item_pedido_data = Item_Pedido_Data(quantidade = item_pedido.quantidade,
                                        pedido_id = item_pedido.pedido.id,
                                        produto_id = item_pedido.produto.id)

    db.add(item_pedido_data)
    db.commit()
    db.refresh(item_pedido_data)

    return item_pedido

def obter_item_pedido_por_nome(nome: str, db: Session):
    item_pedido  =db.query(Item_Pedido_Data).filter(Item_Pedido_Data.nome.ilike(f"%{nome}%")).all()
    return item_pedido

def obter_item_pedido(id: int, db: Session):
    item_pedido = db.query(Item_Pedido_Data).filter(Item_Pedido_Data.id == id).first()

    if not item_pedido:
        raise HTTPException(status_code=404, detail=f"Item do pedido não encontrado!")
    
    return item_pedido

def alterar_item_pedido(id: int, item_pedido: Item_Pedido, db: Session):
    item_pedido_data = db.query(Item_Pedido).filter(Item_Pedido.id == id).first()

    if not item_pedido_data:
        raise HTTPException(status_code=404, detail=f"Item do pedido não encontrado!")
    
    item_pedido_data.quantidade = item_pedido.quantidade
    item_pedido_data.produto_id = item_pedido.produto.id
    item_pedido_data.pedido_id = item_pedido.pedido.id
    

    db.commit()
    db.refresh(item_pedido_data)

    return item_pedido_data

def excluir_item_pedido(id: int, db: Session):

    item_pedido_data = db.query(Item_Pedido_Data).filter(Item_Pedido_Data.id == id).first()

    if not item_pedido_data:
        raise HTTPException(status_code=404, detail=f"Item do pedido não encontrado!")
    
    db.delete(item_pedido_data)
    db.commit()
    
    return {"Mensagem": "Item do pedido excluído com sucesso"}

