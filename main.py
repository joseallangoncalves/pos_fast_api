from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI rodando com sucesso!"}

@app.get("/status")
def get_status():
    return {"status": "online"}

# Passando o número 1 e 2 no corpo da requisição
@app.get(path="/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}
