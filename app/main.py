from fastapi import FastAPI

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
    return {
        "id": produto_id,
        "nome": "Notebook",
        "preco": 4500.00,
    }
