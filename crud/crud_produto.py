
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Produto_Data
from schemas import Produto

def criar_produto(produto: Produto, db: Session):
    produto_data = Produto_Data(nome= produto.nome, preco= produto.preco, categoria_id = produto.categoria.id)

    db.add(produto_data)
    db.commit()
    db.refresh(produto_data)

    return produto_data

def obter_produto_por_nome(nome: str, db: Session):
    produto = db.query(Produto_Data).filter(Produto_Data.nome.ilike(f"%{nome}%")).all()
    return produto

def obter_produto(id: int, db: Session):
    produto = db.query(Produto_Data).filter(Produto_Data.id == id).first()

    if not produto:
        raise HTTPException(status_code=404, detail=f"Produto não encontrado!")
    
    return produto

def alterar_produto(id: int, produto: Produto, db: Session):
    produto_data = db.query(Produto_Data).filter(Produto_Data.id == id).first()

    if not produto_data:
        raise HTTPException(status_code=404, detail=f"Produto não encontrado!")
    
    produto_data.nome = produto.nome
    produto_data.preco = produto.preco
    produto_data.categoria_id = produto.categoria.id

    db.commit()
    db.refresh(produto_data)

    return produto_data

def excluir_produto(id: int, db: Session):

    produto_data = db.query(Produto_Data).filter(Produto_Data.id == id).first()

    if not produto_data:
        raise HTTPException(status_code=404, detail=f"Produto não encontrado!")
    
    db.delete(produto_data)
    db.commit()
    
    return {"Mensagem": "Produto excluído com sucesso"}

