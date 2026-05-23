from fastapi import status, HTTPException
import logging
from groq import Groq
import os


API_TOKEN = "123"


def get_logger():

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("fastapi")

    return logger


def common_api_token(api_token: str):
    logger = get_logger()
    logger.info(f"Token recebido: {api_token}")

    if api_token != API_TOKEN:
        logger.warning("Token de autenticação inválido")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação inválido",
        )

    logger.info("Token de autenticação válido")
    return {"api_token": api_token}


def execute_prompt(prompt: str, model: str = "llama-3.1-8b-instant"):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    resultado = chat_completion.choices[0].message.content

    return resultado