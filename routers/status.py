from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_status import criar_status, obter_status, alterar_status, excluir_status
from database import get_db
from models import Status_Data
from schemas import Status

router = APIRouter(prefix="/status", tags=["Status"])

@router.post("/",
            response_model=Status,
            summary="Criar Status",
            description="Cria status de cliente caso passar pelas regras",
            responses={500:{"description": "Erro ao criar status de cliente"}}
        )
def criar(status: Status, db = Depends(get_db)):
    return criar_status(status, db)


@router.get("/{id}",
            response_model=Status,
            summary="Obter Status",
            description="Buscar um Status",
            responses={500:{"description": "Erro ao buscar de Status"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_status(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Status{e}!!')

@router.put("/{id}",
            response_model=Status,
            summary="Alterar Status",
            description="Alterar registro de Status",
            responses={500:{"description": "Erro ao alterar de Status"}}                 
            ) 

def alterar(id: int, status: Status, db = Depends(get_db)):
    try:
        status_data = db.query(Status_Data).filter(Status_Data.id == id).first()
    
        if not status_data:
            raise HTTPException(status_code=404, detail=f'Status não encontrado!!')
        
        status_data.descricao = status.descricao
      
        
        db.commit()
        db.refresh(status_data)
    
        return status_data


    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar Status{e}!!')

@router.delete("/{id}",
            summary="Excluir Status",
            description="Excluir registro de Status",
            responses={500:{"description": "Erro ao excluir status"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_status(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir status{e}!!')