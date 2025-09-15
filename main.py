from fastapi import FastAPI


from database import Base, engine
from routers import categoria, status, cliente, produto, insumos, item_pedido, pedido


Base.metadata.create_all(engine)

app = FastAPI()


app.include_router(status.router)
app.include_router(cliente.router)
app.include_router(produto.router)
app.include_router(categoria.router)
app.include_router(pedido.router)
app.include_router(item_pedido.router)
app.include_router(insumos.router)

