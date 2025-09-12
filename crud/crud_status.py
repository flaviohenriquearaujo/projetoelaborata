from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Status_Data
from schemas import Status

def criar_status(status: Status, db: Session):
    status_data = Status_Data(descricao = status.descricao)

    db.add(status_data)
    db.commit()
    db.refresh(status_data)

    return status_data


def obter_status(id: int, db: Session):
    status = db.query(Status_Data).filter(Status_Data.id == id).first()

    if not status:
        raise HTTPException(status_code=404, detail=f"Status não encontrado!")
    
    return status

def alterar_status(id: int, status: Status, db: Session):
    status_data = db.query(Status_Data).filter(Status_Data.id == id).first()

    if not status_data:
        raise HTTPException(status_code=404, detail=f"Status não encontrado!")
    
    status_data.descricao = status.descricao
    
    db.commit()
    db.refresh(status_data)

    return status_data

def excluir_status(id: int, db: Session):

    status_data = db.query(Status_Data).filter(Status_Data.id == id).first()

    if not status_data:
        raise HTTPException(status_code=404, detail=f"Status não encontrado!")
    
    db.delete(status_data)
    db.commit()
    
    return {"Mensagem": "Status excluído com sucesso"}








