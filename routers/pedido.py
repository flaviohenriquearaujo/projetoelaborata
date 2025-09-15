from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_pedidos import criar_pedido, excluir_pedido, alterar_pedido, obter_pedido
from database import get_db
from models import Pedido_Data
from schemas import Pedido, Cliente

router = APIRouter(prefix="/pedido", tags=["Pedidos"])

@router.post("/",
            response_model=Pedido,
            summary="Criar Registro de pedido",
            description="Cria um registro de pedido caso passar pelas regras",
            responses={500:{"description": "Erro ao criar registro de pedido"}}
        )
def criar(pedido: Pedido, db = Depends(get_db)):
    return criar_pedido(pedido, db)


@router.get("/busca_por_cliente",
            response_model=list[Pedido],
            summary="Buscar pedido por nome do cliente",
            description="Buscar por nome do cliente",
            responses={500:{"description": "Erro ao buscar pedido por nome do cliente"}}
        )




def obter_pedidos_por_nome_cliente(nome_cliente: str, db: Session = Depends(get_db)):
    try:
        cliente = db.query(Cliente).filter(Cliente.nome == nome_cliente).first()
        
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        
        pedidos = db.query(Pedido_Data).filter(Pedido_Data.cliente_id == cliente.id).all
        
        return pedidos (nome_cliente, db)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter cliente{e}!!')







@router.get("/{id}",
            response_model=Pedido,
            summary="Obter pedido",
            description="Buscar um pedido",
            responses={500:{"description": "Erro ao buscar pedido"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_pedido(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter pedido. # {e} #!!')

@router.put("/{id}",
            response_model=Pedido,
            summary="Alterar pedido",
            description="Alterar registro de pedido",
            responses={500:{"description": "Erro ao alterar pedido"}}                 
            ) 

def alterar(id: int, pedido: Pedido, db = Depends(get_db)):
    try:
        pedido_data = db.query(Pedido_Data).filter(Pedido_Data.id == id).first()
    
        if not pedido_data:
            raise HTTPException(status_code=404, detail=f'pedido não encontrado!!')
        
        pedido_data.nr_pedido = pedido.nr_pedido,
        pedido_data.data_pedido = pedido.data_pedido,
        pedido_data.data_entrega = pedido.data_entrega,
        pedido_data.tipo_entrega = pedido.tipo_entrega,
        pedido_data.observacoes = pedido.observacoes,
        pedido_data.cliente_id = pedido.cliente.id,
        pedido_data.status_id = pedido.status.id
            
        db.commit()
        db.refresh(pedido_data)
    
        return pedido_data


    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar pedido. # {e} #!!')

@router.delete("/{id}",
            response_model=Pedido,
            summary="Excluir pedido",
            description="Excluir registro de pedido",
            responses={500:{"description": "Erro ao excluir pedido"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_pedido(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir pedido. # {e} #!!')
   
   