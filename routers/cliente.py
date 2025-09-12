from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_cliente import criar_cliente, obter_cliente, obter_cliente_por_nome, alterar_cliente, excluir_cliente
from database import get_db
from models import Cliente_Data
from schemas import Cliente

router = APIRouter(prefix="/cliente", tags=["Clientes"])

@router.post("/",
            response_model=Cliente,
            summary="Criar Registro de Cliente",
            description="Cria um registro de cliente caso passar pelas regras",
            responses={500:{"description": "Erro ao criar registro de cliente"}}
        )
def criar(cliente: Cliente, db = Depends(get_db)):
    return criar_cliente(cliente, db)


@router.get("/buscar",
            response_model=list[Cliente]
            
            pass)