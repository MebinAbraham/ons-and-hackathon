"""
Uses the fine-tuned model to make api calls
"""

import logging
import os

import openai
from dotenv import load_dotenv

from utilities import SYSTEM_MESSAGE, format_response, generate_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
FINE_TUNE_ID = os.getenv("FINE_TUNE_ID")
logger = logging.getLogger("Hackathon")


def predict(year: int, inflation: float, income: float) -> dict:
    """
    Uses the year, inflation and income to format a prompt to send to the fine-tuned model
    returns the categories and expenditure as a dictionary, or an error if the response cannot be parsed.
    """
    prompt = generate_prompt(year=year, inflation=inflation, income=income)
    temporary_extra = "Please output your answer without any extra information in the format: food: 100, clothing: 100, entertainment: 100, transport: 100"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            SYSTEM_MESSAGE,
            {"role": "user", "content": prompt + "\n" + temporary_extra},
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
    print(predict(2020, 0.02, 1000))
