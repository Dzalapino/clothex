from fastapi.testclient import TestClient
from main import app
from database.schemas import LocalProduct as LocalProductSchema

client = TestClient(app)


def test_get_all_local_products():
    response = client.get("/local_products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_local_product():
    local_product = LocalProductSchema(id=1, amount_in_stock=10)
    response = client.post("/local_products/", json=local_product.dict())
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["amount_in_stock"] == 10.0


# TODO: Test patch for amount in stock


def test_delete_local_product():
    response = client.delete("/local_products/1")
    assert response.status_code == 200
