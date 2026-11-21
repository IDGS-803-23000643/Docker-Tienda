from fastapi.testclient import TestClient

from api import app


client = TestClient(app)


def test_inicio():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"mensaje": "Tienda DepOps 2.0"}


def test_calcular_compra():
    response = client.post("/compra", json={"precio": 100, "descuento": 10})

    assert response.status_code == 200
    assert response.json() == {"subtotal": 90.0, "total": 104.4}


def test_rechaza_precio_negativo():
    response = client.post("/compra", json={"precio": -1, "descuento": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "precio invalido"}


def test_rechaza_descuento_fuera_de_rango():
    response = client.post("/compra", json={"precio": 100, "descuento": 101})

    assert response.status_code == 400
    assert response.json() == {"detail": "Descuento invalido"}
