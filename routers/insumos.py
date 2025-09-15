from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_insumos import criar_insumo, obter_insumo, obter_insumo_por_nome, excluir_insumo, alterar_insumo
from database import get_db
from models import Insumos_Data
from schemas import Insumos

router = APIRouter(prefix="/insumos", tags=["Insumos"])

@router.post("/",
            response_model=Insumos,
            summary="Criar Registro de insumo",
            description="Cria um registro de insumo caso passar pelas regras",
            responses={500:{"description": "Erro ao criar registro de insumo"}}
        )
def criar(insumo: Insumos, db = Depends(get_db)):
    return criar_insumo(insumo, db)


@router.get("/buscar",
            response_model=list[Insumos],
            summary="Buscar insumo por parte do nome",
            description="Buscar insumo",
            responses={500:{"description": "Erro ao buscar insumo"}}
        )
def obter_por_nome(nome: str, db = Depends(get_db)):
    try:
        return obter_insumo_por_nome(nome, db)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter insumo. # {e} #!!')

@router.get("/{id}",
            response_model=Insumos,
            summary="Obter insumo",
            description="Buscar um insumo",
            responses={500:{"description": "Erro ao buscar insumo"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_insumo(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter insumo. # {e} #!!')

@router.put("/{id}",
            response_model=Insumos,
            summary="Alterar insumo",
            description="Alterar registro de insumo",
            responses={500:{"description": "Erro ao alterar insumo"}}                 
            ) 

def alterar(id: int, insumo: Insumos, db = Depends(get_db)):
    try:
        insumo_data = db.query(Insumos_Data).filter(Insumos_Data.id == id).first()
    
        if not insumo_data:
            raise HTTPException(status_code=404, detail=f'insumo não encontrado!!')
        
        insumo_data.nome = insumo.nome
        insumo_data.quantidade = insumo.quantidade
        insumo_data.custo_unitario = insumo.custo_unitario
        insumo_data.custo_total = insumo.custo_total
        insumo_data.pedido_id = insumo.pedido.id
        insumo_data.produto_id = insumo.produto.id
        
        db.commit()
        db.refresh(insumo_data)
    
        return insumo_data


    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar insumo. # {e} # !!')

@router.delete("/{id}",
            response_model=Insumos,
            summary="Excluir insumo",
            description="Excluir registro de insumo",
            responses={500:{"description": "Erro ao excluir insumo"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_insumo(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir insumo. # {e} # !!')
   
   