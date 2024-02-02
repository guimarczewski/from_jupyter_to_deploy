from fastapi import FastAPI

# importar classes - coloca o ponto antes pois está no mesmo repositorio
from .schema import ProdutosSchema
from .routes import router
from typing import List


app = FastAPI()

app.include_router(router)
