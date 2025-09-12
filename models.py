
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship



class Cliente_Data(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable = False)
    endereco = Column(String, nullable = False)
    status_id = Column(Integer, ForeignKey("status.id"))

    status = relationship("Status_Data")

# class Produto_Data(Base):
#     __tablename__ = "produtos"

#     id = Column(Integer, primary_key = True, index = True)
#     nome = Column(String, nullable = False)
#     preco = Column(Float, nullable = False)
    
#     categoria_id = Column(Integer, ForeignKey("categoria_de_produtos.id"), nullable = False)

#     categoria = relationship("Categoria_Produtos_Data")

# class Categoria_Produtos_Data(Base):
#     __tablename__ = "categoria_de_produtos"

#     id = Column(Integer, primary_key = True, index = True)
#     nome = Column(String, nullable = False)
    
# class Pedido_Data(Base):
#     __tablename__ = "pedido"

#     id = Column(Integer, primary_key = True, index = True)
#     data_pedido = Column(Date, nullable = False)
#     data_entrega = Column(Date, nullable = False)
#     tipo_entrega = Column(String, nullable = False)
#     status = Column(String, nullable = False)
#     observacoes = Column(String)
    
#     cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable = False)

#     cliente = relationship("Cliente_Data")

# class Item_Pedido_Data(Base):
#     __tablename__ = "itens_do_pedido"

#     id = Column(Integer, primary_key = True, index = True)
#     quantidade = Column(Integer, nullable = False)

#     pedido_id = Column(Integer, ForeignKey('pedido.id'), nullable = False)
#     produto_id = Column(Integer, ForeignKey('produtos.id'), nullable = False)

#     pedido = relationship("Pedido_Data")
#     produto = relationship("Produtos_Data")

# class Insumos_Data(Base):
#     __tablename__ = "insumos"

#     id = Column(Integer, primary_key = True, index = True)
#     nome = Column(String, nullable = False)
#     quantidade = Column(Float, nullable = False)
#     custo_unitario = Column(Float, nullable = False)
#     custo_total = Column(Float, nullable = False)
    
#     pedido_id = Column(Integer, ForeignKey('pedido.id'), nullable = False)
#     produto_id = Column(Integer, ForeignKey('produtos.id'), nullable = False)

#     pedido = relationship("Pedido_Data")
#     produto = relationship("Produtos_Data")

class Status_Data(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key = True, index = True)
    descricao = Column(String, nullable = False)
