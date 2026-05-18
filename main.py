from fastapi import HTTPException
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

API_TOKEN = "123"


# Passando o número 1 e 2 no corpo da requisição
class Numeros(BaseModel):
    numero1: int = Field(5, description="Primeiro número")
    numero2: int = Field(3, description="Segundo número")
    api_token: str = Field(..., description="Token de autenticação")

# Passando o número 1 e 2 no corpo da requisição
class Resultado(BaseModel):
    resultado: int

@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI rodando com sucesso!"}

@app.get("/status")
def get_status():
    return {"status": "online"}

# Passando o número 1 e 2 no corpo da requisição
@app.get(
     path="/soma/v1/{numero1}/{numero2}",
     summary="Soma dois números inteiros",
     description="Recebe dois números inteiros e retorna a soma",
     tags=["Operações matemáticas"]
    )
def soma(numero1: int, numero2: int, api_token: str):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token de autenticação inválido")

    total = numero1 + numero2
    if total < 0 :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Resultado negativo")
    return {"resultado": total}

# Passando o número 1 e 2 no corpo da requisição
@app.post(
    path="/soma/v2",
    response_model=Resultado,
    status_code=status.HTTP_200_OK,
    tags=["Operações matemáticas"],
    summary="Será descontinuado em 15/06/2026",
    deprecated=True
)
def soma_formato2(numero1: int, numero2: int, api_token: str):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token de autenticação inválido")

    total = numero1 + numero2
    return {"resultado": total}


@app.post(
     path="/soma/v3",
     response_model=Resultado,
     summary="Soma dois números",
     description="Soma dois números inteiros e retorna o resultado",
     tags=["Operações matemáticas"],
     status_code=status.HTTP_200_OK,
     response_description="Prcessamento feito com sucesso!"
     )
def soma_formato3(numeros: Numeros):
    if numeros.api_token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token de autenticação inválido")
    if numeros.numero1 < 0 or numeros.numero2 < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Números devem ser positivos")
    
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}
