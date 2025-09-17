from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_categoria import criar_categoria, obter_categoria, obter_categoria_por_nome, excluir_categoria, alterar_categoria
from database import get_db
from models import Categoria_Produtos_Data
from schemas import Categoria_Produtos

router = APIRouter(prefix="/categoria", tags=["Categoria de Produtos"])

@router.post("/",
            response_model=Categoria_Produtos,
            summary="Criar Registro de Categoria de Produtos",
            description="Cria um registro de Categoria de Produtos caso passar pelas regras",
            responses={500:{"description": "Erro ao criar registro de Categoria de Produtos"}}
        )
def criar(categoria: Categoria_Produtos, db = Depends(get_db)):
    return criar_categoria(categoria, db)


@router.get("/buscar",
            response_model=list[Categoria_Produtos],
            summary="Buscar Categoria de Produtos por parte do nome",
            description="Buscar Categoria de Produtos",
            responses={500:{"description": "Erro ao buscar Categoria de Produtos"}}
        )
def obter_por_nome(nome: str, db = Depends(get_db)):
    try:
        return obter_categoria_por_nome(nome, db)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Categoria de Produtos. # {e} #!!')

@router.get("/{id}",
            response_model=Categoria_Produtos,
            summary="Obter Categoria de Produtos",
            description="Buscar uma Categoria de Produtos",
            responses={500:{"description": "Erro ao buscar Categoria de Produtos"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_categoria(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Categoria de Produtos. # {e} #!!')

@router.put("/{id}",
            response_model=Categoria_Produtos,
            summary="Alterar Categoria de Produtos",
            description="Alterar registro de Categoria de Produtos",
            responses={500:{"description": "Erro ao alterar Categoria de Produtos"}}                 
            ) 

def alterar(id: int, categoria: Categoria_Produtos, db = Depends(get_db)):
    try:
        categoria_data = db.query(Categoria_Produtos_Data).filter(Categoria_Produtos_Data.id == id).first()
    
        if not categoria_data:
            raise HTTPException(status_code=404, detail=f'Categoria de Produtos não encontrada!!')
        
        categoria_data.nome = categoria.nome
        
        db.commit()
        db.refresh(categoria_data)
    
        return categoria_data

    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar Categoria de Produtos. # {e} #!!')

@router.delete("/{id}",
            summary="Excluir Categoria de Produtos",
            description="Excluir registro de Categoria de Produtos",
            responses={500:{"description": "Erro ao excluir Categoria de Produtos"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_categoria(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir Categoria de Produtos. # {e} # !!')
   
   