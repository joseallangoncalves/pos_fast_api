from fastapi import status
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel, Field

app = FastAPI(
    title="Aula",
    summary="API desenvolvida durante a aula de Construção de APIs para IA",
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Rogério Rodrigues Carvalho",
        "url": "http://github.com/rogerior/",
        "email": "rogerior@ufg.br",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI rodando com sucesso!"}

@app.get("/status")
def get_status():
    return {"status": "online"}

# Passando o número 1 e 2 no corpo da requisição
@app.get(path="/soma/{numero1}/{numero2}", tags=["Operações matemáticas"])
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Passando o número 1 e 2 no corpo da requisição
@app.post("/soma_formato2", tags=["Operações matemáticas"])
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição
class Numeros(BaseModel):
    numero1: int = Field(..., gt=0)
    numero2: int = Field(..., gt=0)

# Passando o número 1 e 2 no corpo da requisição
class Resultado(BaseModel):
    resultado: int

@app.post("/soma_formato3", 
          response_model=Resultado,
          summary="Soma dois números",
          description="Soma dois números inteiros e retorna o resultado",
          tags=["Operações matemáticas"],
        status_code=status.HTTP_200_OK,
        response_description="Prcessamento feito com sucesso!",
        )
        
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}
