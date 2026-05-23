from pydantic import BaseModel, Field
from enum import Enum


class Numeros(BaseModel):
    numero1: int = Field(5, description="O primeiro número a ser somado")
    numero2: int = Field(3, description="O segundo número a ser somado")


class Resultado(BaseModel):
    resultado: int = Field(..., description="O resultado da soma dos dois números")


class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


class Historia(BaseModel):
    tema: str = Field(..., description="O tema da história a ser gerada")