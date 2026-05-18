from enum import Enum
from fastapi import HTTPException, Depends
from fastapi import status
from fastapi import FastAPI
from pydantic import BaseModel, Field
import logging
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s -(levelname)s - %(message)s"
)
logger = logging.getLogger("fastapi")
# logger.info('Mensagem informativa')
# logger.warning('Mensagem de alerta')
# logger.error('Mensagem de erro')
# logger.critical('Mensagem crítica')
# logger.debug('Mensagem de debug')
# logger.exception('Mensagem de exceção')
# logger.fatal('Mensagem de erro fatal')


API_TOKEN = "123"


def common_api_token(api_token: str):
    logger.info("Token recebido: %s", api_token)
    # print("O token recebido foi: ", api_token)

    if api_token != API_TOKEN:
        logger.warning("Token de autenticação inválido: %s", api_token)
        # print("Token de autenticação inválido")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido"
        )

    logger.info("Token de autenticação válido: %s", api_token)
    # print("Token de autenticação válido")
    return {"api_token": api_token}


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
    dependencies=[Depends(common_api_token)],
)


# Passando o número 1 e 2 no corpo da requisição
class Numeros(BaseModel):
    numero1: int = Field(5, description="Primeiro número")
    numero2: int = Field(3, description="Segundo número")


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
    tags=["Operações matemáticas"],
)
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    if total < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Resultado negativo"
        )
    return {"resultado": total}


# Passando o número 1 e 2 no corpo da requisição
@app.post(
    path="/soma/v2",
    response_model=Resultado,
    status_code=status.HTTP_200_OK,
    tags=["Operações matemáticas"],
    summary="Será descontinuado em 15/06/2026",
    deprecated=True,
)
def soma_formato2(numero1: int, numero2: int, api_token: str):
    total = numero1 + numero2
    return {"resultado": total}


@app.post(
    path="/soma/v3",
    response_model=Resultado,
    summary="Soma dois números",
    description="Soma dois números inteiros e retorna o resultado",
    tags=["Operações matemáticas"],
    status_code=status.HTTP_200_OK,
    response_description="Prcessamento feito com sucesso!",
)
def soma_formato3(numeros: Numeros):

    if numeros.numero1 < 0 or numeros.numero2 < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Números devem ser positivos",
        )

    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}


class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


@app.post("/operacao_matematica", tags=["Operações matemáticas"])
def operacao_matematica(numeros: Numeros, operacao: TipoOperacao):

    if operacao == TipoOperacao.soma:
        resultado = numeros.numero1 + numeros.numero2
    elif operacao == TipoOperacao.subtracao:
        resultado = numeros.numero1 - numeros.numero2
    elif operacao == TipoOperacao.multiplicacao:
        resultado = numeros.numero1 * numeros.numero2
    elif operacao == TipoOperacao.divisao:
        resultado = numeros.numero1 / numeros.numero2

    return {"resultado": resultado}


class Historia(BaseModel):
    Tema: str = Field(..., description="Tema da história")


@app.post("/gerar_historia")
def gerar_historica(historia: Historia):

    prompt = f"Escreva uma história sobre o tema:  {historia.Tema}"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    historia = chat_completion.choices[0].message.content
    return {"historia": historia}
