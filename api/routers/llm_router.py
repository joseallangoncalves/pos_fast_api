from fastapi import APIRouter
from api.models import Historia
from api.utils import execute_prompt


router = APIRouter()


@router.post("/gerar_historia")
def gerar_historica(historia: Historia):
    prompt = f"Escreva uma história sobre o tema:  {historia.Tema}"
    historia = execute_prompt(prompt)
    return {"historia": historia}