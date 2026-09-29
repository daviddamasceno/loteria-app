from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_sortear_success():
    payload = {
        "range_max": 60,
        "quantidade": 6
    }
    response = client.post("/api/sortear", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "numeros" in data
    numeros = data["numeros"]
    
    assert len(numeros) == 6
    assert len(set(numeros)) == 6  # Sem números duplicados
    assert all(1 <= n <= 60 for n in numeros)
    # Verifica se os números estão ordenados
    assert numeros == sorted(numeros)

def test_sortear_erro_quantidade_maior_que_range():
    payload = {
        "range_max": 10,
        "quantidade": 15
    }
    response = client.post("/api/sortear", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "A quantidade não pode ser maior que o range."

def test_sortear_erro_valores_negativos():
    payload = {
        "range_max": 0,
        "quantidade": 5
    }
    response = client.post("/api/sortear", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Os valores devem ser maiores que zero."

    payload2 = {
        "range_max": 50,
        "quantidade": -1
    }
    response2 = client.post("/api/sortear", json=payload2)
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Os valores devem ser maiores que zero."
