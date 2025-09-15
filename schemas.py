


from pydantic import BaseModel
from datetime import date


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
    id_nr_pedido: int
    data_pedido: date
    data_entrega: date
    tipo_entrega: str
    observacoes: str
    cliente: Cliente
    status: Status

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

