"""
Uses the fine-tuned model to make api calls
"""

import logging
import os
from random import randint

import openai
from dotenv import load_dotenv

from utilities import SYSTEM_MESSAGE, format_response, generate_prompt

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FINE_TUNE_ID = os.getenv("FINE_TUNE_ID")
logger = logging.getLogger("Hackathon")
openai.api_key = OPENAI_API_KEY

PROMPT_ENGINEERING_101 = """
Use the input data to predict yearly expenditure. Please output your answer without any extra information in the format: food: a; clothing: b; entertainment: c; transport: d
"""

def predict(*, year: int, inflation: float, income: float) -> dict:
    """
    Uses the year, inflation and income to format a prompt to send to the fine-tuned model
    returns the categories and expenditure as a dictionary, or an error if the response cannot be parsed.
    """
    prompt = generate_prompt(year=year, inflation=inflation, income=income)
    temporary_extra = PROMPT_ENGINEERING_101
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            SYSTEM_MESSAGE,
            {"role": "user", "content": prompt + temporary_extra},
        ],
    )
    response = completion.choices[0].message["content"]
    logger.info(f"{response=}")
    # it's a bit flaky so try a few times
    for _ in range(5):
        try:
            result = format_response(response)
            logger.info("API call successful")
            result["success"] = True
            return result
        except ValueError:
            logger.error("error: Unable to parse response")
            print(response)
    logger.info("API call unsuccessful")

    return {
        "food": randint(0, 1000),
        "clothing": randint(0, 1000),
        "entertainment": randint(0, 1000),
        "transport": randint(0, 1000),
        "success": False,
    }


if __name__ == "__main__":
    print(predict(year=2020, inflation=0.02, income=1000))
