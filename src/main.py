import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 57000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

@app.get("/somar/{a}/{b}")
async def somar(a: int, b: int):
    return {"resultado": a + b}

@app.get("/subtrair/{a}/{b}")
async def subtrair(a: int, b: int):
    return {"resultado": a - b}

@app.get("/multiplicar/{a}/{b}")
async def multiplicar(a: int, b: int):
    return {"resultado": a * b}

@app.get("/dividir/{a}/{b}")
async def dividir(a: int, b: int):
    if b == 0:
        return {"erro": "Divisão por zero não é permitida"}
    return {"resultado": a / b}

@app.get("/dobro/{a}")
async def dobro(a: int):
    return {"resultado": a * 2}
