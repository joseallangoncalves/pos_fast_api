from fastapi import APIRouter, HTTPException, status

from api.models import Numeros, Resultado, TipoOperacao


router = APIRouter()


# http://127.0.0.1:8000/soma/3/2
@router.post(
    "/soma/v1/{numero1}/{numero2}",
    deprecated=True,
    summary="Será descontinuado em 15/06",
)
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# http://127.0.0.1:8000/soma_formato2?numero1=3&numero2=2
@router.post("/soma/v2")
def soma_formato2(numero1: int, numero2: int, api_token: str):

    total = numero1 + numero2
    return {"resultado": total}


# 'http://127.0.0.1:8000/soma_formato3'
#   -d '{
#   "numero1": 3,
#   "numero2": 2
# }'
@router.post(
    "/soma/v3",
    response_model=Resultado,
    summary="Soma de dois números utilizando um modelo de dados",
    description="Este endpoint recebe um modelo de dados contendo dois números e retorna o resultado da soma desses números.",
    status_code=status.HTTP_200_OK,
    response_description="Processamento realizado com sucesso",
)
def soma_formato3(numeros: Numeros):

    # Se o numero1 for negativo, retorna um erro
    if numeros.numero1 < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O número 1 não pode ser negativo",
        )

    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}


@router.post("/operacao_matematica/v1", tags=["Operações matemáticas"])
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