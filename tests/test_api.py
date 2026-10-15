from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {
        "mensagem": "API funcionando com sucesso"
    }


def test_health():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_consultar_produto():
    resposta = client.get("/produtos/1")
    assert resposta.status_code == 200
    assert resposta.json()["id"] == 1
    assert resposta.json()["nome"] == "Notebook"

    
def test_consultar_produto_id_invalido():
    resposta = client.get("/produtos/abc")
    assert resposta.status_code == 422
