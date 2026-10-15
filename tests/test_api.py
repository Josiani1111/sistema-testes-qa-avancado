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
    assert resposta.json()["preco"] == 4500.00
    assert isinstance(resposta.json()["preco"], (int, float))
    assert resposta.json()["preco"] > 0

    
def test_consultar_produto_id_invalido():
    resposta = client.get("/produtos/abc")
    assert resposta.status_code == 422

    
def test_produto_inexistente():
    resposta = client.get("/produtos/999")

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Produto não encontrado"
    }

