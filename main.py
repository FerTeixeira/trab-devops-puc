from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    """Rota de exemplo que retorna uma mensagem."""
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    """Rota de teste que retorna status e número."""
    return {"teste": "deu certo"}