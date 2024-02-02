from pydantic import BaseModel, PositiveInt
from typing import Optional

class ProdutosSchema(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveInt
