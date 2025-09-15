
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Categoria_Produtos_Data
from schemas import Categoria_Produtos

def criar_categoria(categoria: Categoria_Produtos, db: Session):
    categoria_data = Categoria_Produtos_Data(nome = categoria.nome)

    db.add(categoria_data)
    db.commit()
    db.refresh(categoria_data)

    return categoria_data

def obter_categoria_por_nome(nome: str, db: Session):
    categoria  =db.query(Categoria_Produtos_Data).filter(Categoria_Produtos_Data.nome.ilike(f"%{nome}%")).all()
    return categoria

def obter_categoria(id: int, db: Session):
    categoria = db.query(Categoria_Produtos_Data).filter(Categoria_Produtos_Data.id == id).first()

    if not categoria:
        raise HTTPException(status_code=404, detail=f"Categoria não encontrada!")
    
    return categoria

def alterar_categoria(id: int, categoria: Categoria_Produtos, db: Session):
    categoria_data = db.query(Categoria_Produtos).filter(Categoria_Produtos.id == id).first()

    if not categoria_data:
        raise HTTPException(status_code=404, detail=f"Categoria não encontrada!")
    
    categoria_data.nome = categoria.nome
   
    db.commit()
    db.refresh(categoria_data)

    return categoria_data

def excluir_categoria(id: int, db: Session):

    categoria_data = db.query(Categoria_Produtos_Data).filter(Categoria_Produtos_Data.id == id).first()

    if not categoria_data:
        raise HTTPException(status_code=404, detail=f"Categoria não encontrada!")
    
    db.delete(categoria_data)
    db.commit()
    
    return {"Mensagem": "Categoria excluída com sucesso"}

