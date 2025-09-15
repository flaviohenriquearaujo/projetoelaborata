from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from crud.crud_item_pedidos import criar_item_pedido, obter_item_pedido, excluir_item_pedido, alterar_item_pedido, obter_item_pedido_por_nome
from database import get_db
from models import Item_Pedido_Data
from schemas import Item_Pedido

router = APIRouter(prefix="/item_pedido", tags=["Itens de Pedidos"])

@router.post("/",
            response_model=Item_Pedido,
            summary="Criar Registro de Item do Pedido",
            description="Cria um registro de Item do Pedido caso passar pelas regras",
            responses={500:{"description": "Erro ao criar registro de Item do Pedido"}}
        )
def criar(item_pedido: Item_Pedido, db = Depends(get_db)):
    return criar_item_pedido(item_pedido, db)


@router.get("/buscar",
            response_model=list[Item_Pedido],
            summary="Buscar Item do Pedido por parte do nome",
            description="Buscar Item do Pedido",
            responses={500:{"description": "Erro ao buscar Item do Pedido"}}
        )
def obter_por_nome(quantidade: int, db = Depends(get_db)):
    try:
        return obter_item_pedido_por_nome(quantidade, db)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Item do Pedido # {e} # !!')

@router.get("/{id}",
            response_model=Item_Pedido,
            summary="Obter Item do Pedido",
            description="Buscar um Item do Pedido",
            responses={500:{"description": "Erro ao buscar Item do Pedido"}}                 
            )

def obter(id: int, db = Depends(get_db)):
    try:
        
        return obter_item_pedido(id, db)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Erro ao obter Item do Pedido. # {e} # !!')

@router.put("/{id}",
            response_model=Item_Pedido,
            summary="Alterar Item do Pedido",
            description="Alterar registro de Item do Pedido",
            responses={500:{"description": "Erro ao alterar Item do Pedido"}}                 
            ) 

def alterar(id: int, item_pedido: Item_Pedido, db = Depends(get_db)):
    try:
        item_pedido_data = db.query(Item_Pedido_Data).filter(Item_Pedido_Data.id == id).first()
    
        if not item_pedido_data:
            raise HTTPException(status_code=404, detail=f'Item do Pedido não encontrado!!')
        
        item_pedido_data.quantidade = item_pedido.quantidade
        item_pedido_data.produto_id = item_pedido.produto.id
        item_pedido_data.pedido_id = item_pedido.pedido.id
        
        db.commit()
        db.refresh(item_pedido_data)
    
        return item_pedido_data


    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao alterar Item do Pedido. # {e} # !!')

@router.delete("/{id}",
            response_model=Item_Pedido,
            summary="Excluir Item do Pedido",
            description="Excluir registro de Item do Pedido",
            responses={500:{"description": "Erro ao excluir Item do Pedido"}}
            )

def excluir(id: int, db = Depends(get_db)):
    try:
        return excluir_item_pedido(id, db)
    
    except Exception as e:
       raise HTTPException(status_code=500, detail=f'Erro ao excluir Item do Pedido. # {e} #!!')
   
   