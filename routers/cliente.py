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
            response_model=list[Cliente],
            summary="Buscar Cliente por parte do nome",
            description="Buscar cliente",
            responses={500:{"description": "Erro ao buscar cliente"}}
        )
def obter_por_nome(nome: str, db = Depends(get_db)):
    try:
        return obter_cliente_por_nome(nome, db)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter cliente{e}!!')

@router.get("/{id}",
            response_model=Cliente,
            summary="Obter Cliente",
            description="Buscar um cliente",
            responses={500:{"description": "Erro ao buscar cliente"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_cliente(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter cliente{e}!!')

@router.put("/{id}",
            response_model=Cliente,
            summary="Alterar Cliente",
            description="Alterar registro de cliente",
            responses={500:{"description": "Erro ao alterar cliente"}}                 
            ) 

def alterar(id: int, cliente: Cliente, db = Depends(get_db)):
    try:
        cliente_data = db.query(Cliente_Data).filter(Cliente_Data.id == id).first()
    
        if not cliente_data:
            raise HTTPException(status_code=404, detail=f'Cliente não encontrado!!')
        
        cliente_data.nome = cliente.nome
        cliente_data.telefone = cliente.telefone
        cliente_data.endereco = cliente.endereco        
        cliente_data.status_id = cliente.status.id
        
        db.commit()
        db.refresh(cliente_data)
    
        return cliente_data


    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar cliente{e}!!')

@router.delete("/{id}",
            response_model=Cliente,
            summary="Excluir Cliente",
            description="Excluir registro de cliente",
            responses={500:{"description": "Erro ao excluir cliente"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_cliente(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir cliente{e}!!')
   
   