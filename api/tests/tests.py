import pytest

from fastapi.testclient import TestClient

from api.app.main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200

def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_create_product():
    product_data = {"id": 1, "titulo": "Cadeira Gamer", "descricao": "Cadeira confortável para fazer live", "preco": 1200.00}
    response = client.post("/produtos", json=product_data)
    assert response.status_code == 200

def test_read_product_by_id():
    response = client.get("/produtos/1")
    assert response.status_code == 200

def test_update_product():
    product_data = {"id": 1, "titulo": "Cadeira Gamer", "descricao": "Cadeira confortável para fazer live", "preco": 1500.00}
    response = client.put("/produtos/1", json=product_data)
    assert response.status_code == 200

def test_delete_product():
    response = client.delete("/produtos/1")
    assert response.status_code == 200
