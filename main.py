from fastapi import FastAPI

from database import Base, engine
from routers import status, cliente


Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(status.router)
app.include_router(cliente.router)
