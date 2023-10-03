"""
Uses the fine-tuned model to make api calls
"""

import logging
import os

import openai
from dotenv import load_dotenv

from utilities import SYSTEM_MESSAGE, format_response, generate_prompt

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FINE_TUNE_ID = os.getenv("FINE_TUNE_ID")
logger = logging.getLogger("Hackathon")
openai.api_key = OPENAI_API_KEY


def predict(*, year: int, inflation: float, income: float) -> dict:
    """
    Uses the year, inflation and income to format a prompt to send to the fine-tuned model
    returns the categories and expenditure as a dictionary, or an error if the response cannot be parsed.
    """
    prompt = generate_prompt(year=year, inflation=inflation, income=income)
    temporary_extra = "\nUse the input data to predict yearly expenditure. Please output your answer without any extra information in the format: food: a, clothing: b, entertainment: c, transport: d"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            SYSTEM_MESSAGE,
            {"role": "user", "content": prompt + temporary_extra},
        ],
    )
    response = completion.choices[0].message["content"]
    print(response)
    logger.info(f"{response=}")
    try:
        return format_response(response)
    except ValueError:
        return {"error": "Unable to parse response"}


if __name__ == "__main__":
    print(predict(year=2020, inflation=0.02, income=1000))
