# Streamlit App with FastAPI + Postgres
[![CI Actions Status](https://github.com/guimarczewski/from_jupyter_to_deploy/workflows/CI/badge.svg)](https://github.com/guimarczewski/from_jupyter_to_deploy/actions)
[![Python 33.11.3](https://img.shields.io/badge/python-3.11.3-blue.svg)](https://www.python.org/downloads/release/python-350/)


## Introduction

This project involves creating and managing a product table in a PostgreSQL database. Using the Python FastAPI library, an API was developed to interact with the database, allowing CRUD (Create, Read, Update, Delete) operations on product data. Operations include GET to retrieve product information, POST to add new products, PUT to update existing product information, and DELETE to remove products.

Furthermore, the bank is connected to an interactive dashboard on Streamlit. This dashboard allows you to view product data, such as the price of each product and various visualization options.

The project is also integrated into a CI/CD pipeline. Tests are run in GitHub Actions whenever a pull request is made, ensuring code quality and integrity. The deployment is carried out using Streamlit for the dashboard and Render for the PostgreSQL database and the API.

To see the API and Dashboard running, you can access the following links:
[API](https://api-workshop-ikez.onrender.com/docs#/)

[Streamlit App](https://workshop-lista-database.streamlit.app/)

## Project Structure

* `api.app`: Contains FastAPI routes and initializes the application.
* `api.tests`: Contains FastAPI tests.
* `database`: Contains the database setup script using sqlalchemy, creating the products table and inserting fictitious data into the table. This script is started with docker-compose, after initializing the container with the postgres database.
* `streamlit`: Streamlit script to create data visualization.
* `create_database_sql`: Original script for database setup using .sql files.

## Usage

### Running the application

You can build and run the application using docker-compose

1. Clone the repository:

```bash
git clone https://github.com/guimarczewski/from_jupyter_to_deploy.git
cd from_jupyter_to_deploy
```

2. Run the docker-compose file:

```bash
docker-compose up --build
```

This will build four Docker images on your host machine:
- postgres - postgres database running on port 5432.
- from_jupyter_to_deploy_setup - container to run the setup_database_script.py, to create the database, table "produtos" e insert the example data. After running the script, the container is closed.
- from_jupyter_to_deploy_api - FastAPI running on port 8000.
- from_jupyter_to_deploy_frontend - Frontend using streamlit, running on port 8501, to connect to the database and display records from the "produtos" table.

This will start the application, and it will be accessible at:
* `api`: http://127.0.0.1:8000
* `streamlit`: http://127.0.0.1:8501
* `postgres`: http://127.0.0.1:5432

### API Endpoints

* `GET /`: Basic root endpoint that returns a Hello World message.
* `GET /produtos`: List all products.
* `GET /produtos/{produto_id}`: Displays a given product based on the produto_id input.
* `POST /produtos`: Insert a new product.
* `PUT /produtos/{produto_id}`: Update a product based on the produto_id input.
* `DELETE /produtos/{produto_id}`: Remove a product based on the produto_id input.

![API](https://github.com/guimarczewski/from_jupyter_to_deploy/blob/main/images/docs_api.png?raw=true)

## Code Snippets

### main.py

```python
from fastapi import FastAPI

# importar classes - coloca o ponto antes pois está no mesmo repositorio
from .schema import ProdutosSchema
from .routes import router
from typing import List


app = FastAPI()

app.include_router(router)
```

### model.py

```python
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)

    class Config:
        orm_mode = True
```

### schema.py

```python
from pydantic import BaseModel, PositiveInt
from typing import Optional

class ProdutosSchema(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveInt

```

### config.py

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# cria a engine postgresql
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

# Cria uma sessão para logar
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Criar a tabela
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)

# Definir uma função geradora para ativar e desativar a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

### routes.py

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutosSchema
from .config import SessionLocal, get_db
from .model import Produto

router = APIRouter()

# vamos criar as rotas que são os endereços
@router.get("/") # request
def ola_mundo(): # response
    return {"Hello":"World"}

@router.get("/produtos", response_model=list[ProdutosSchema]) # request definindo qual schema a lista de saída precisa ter
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all() # SELECT * FROM produtos

# endpoint para pegar os produtos
@router.get("/produtos/{produto_id}", response_model=ProdutosSchema) # request
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.post("/produtos", response_model=ProdutosSchema)
def inserir_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump()) # model_dump transforma o modelo em dicionario
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete("/produtos/{produto_id}", response_model=ProdutosSchema)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
def atualizar_produto(
    produto_id: int, produto_data: ProdutosSchema, db: Session = Depends(get_db)
):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")



```
