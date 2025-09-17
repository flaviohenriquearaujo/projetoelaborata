from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_produto import criar_produto, excluir_produto, alterar_produto, obter_produto, obter_produto_por_nome
from database import get_db
from models import Produto_Data
from schemas import Produto

router = APIRouter(prefix="/produto", tags=["Produtos"])

@router.post("/",
            response_model=Produto,
            summary="Criar Registro de Produto",
            description="Cria um registro de Produto caso passar pelas regras",
            responses={500:{"description": "Erro ao criar registro de Produto"}}
        )
def criar(produto: Produto, db = Depends(get_db)):
    return criar_produto(produto, db)


@router.get("/buscar",
            response_model=list[Produto],
            summary="Buscar Produto por parte do nome",
            description="Buscar Produto",
            responses={500:{"description": "Erro ao buscar de Produto"}}
        )
def obter_por_nome(nome: str, db = Depends(get_db)):
    try:
        return obter_produto_por_nome(nome, db)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Produto{e}!!')

@router.get("/{id}",
            response_model=Produto,
            summary="Obter Produto",
            description="Buscar um Produto",
            responses={500:{"description": "Erro ao buscar de Produto"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_produto(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Produto{e}!!')

@router.put("/{id}",
            response_model=Produto,
            summary="Alterar Produto",
            description="Alterar registro de Produto",
            responses={500:{"description": "Erro ao alterar de Produto"}}                 
            ) 

def alterar(id: int, produto: Produto, db = Depends(get_db)):
    try:
        produto_data = db.query(Produto_Data).filter(Produto_Data.id == id).first()
    
        if not produto_data:
            raise HTTPException(status_code=404, detail=f'Produto não encontrado!!')
        
        produto_data.nome = produto.nome
        produto_data.preco = produto.preco
        produto_data.categoria_id = produto.categoria.id
        
        db.commit()
        db.refresh(produto_data)
    
        return produto_data


    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar Produto{e}!!')

@router.delete("/{id}",
            summary="Excluir Produto",
            description="Excluir registro de Produto",
            responses={500:{"description": "Erro ao excluir Produto"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_produto(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir Produto{e}!!')
   
   