


from pydantic import BaseModel
from datetime import datetime


class Status(BaseModel):
    id: int
    descricao: str
    
class Cliente(BaseModel):
    id: int
    nome: str
    telefone: str
    endereco: str
    status: Status

class Categoria_Produtos(BaseModel):
    id: int
    nome: str

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: Categoria_Produtos

class Pedido(BaseModel):
    id: int
    data_pedido: datetime
    data_entrega: datetime
    tipo_entrega: str
    status: str
    observacoes: str
    cliente: Cliente

class Item_Pedido(BaseModel):
    id: int
    quantidade: int

    pedido: Pedido
    produto: Produto

class Insumos(BaseModel):
    id: int
    nome: str
    quantidade: int
    custo_unitario: float
    custo_total: float
    pedido: Pedido
    produto: Produto

