
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Testes de Qualidade",
    description="API para praticar testes automatizados REST",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"mensagem": "API funcionando com sucesso"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/produtos/{produto_id}")
def consultar_produto(produto_id: int):
    if produto_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado",
        )

    return {
        "id": 1,
        "nome": "Notebook",
        "preco": 4500.00,
    }
