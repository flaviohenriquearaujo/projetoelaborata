from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_status import criar_status
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