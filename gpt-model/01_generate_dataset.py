"""
01 - Generate Dataset
Take the raw data and convert it to the format that gpt requires
"""
import json
from pathlib import Path

import jsonlines
from utilities import INPUT_FIELDS, OUTPUT_FIELDS, SYSTEM_MESSAGE

RAW_DATA_PATH = Path("datasets/raw_data.json")
FORMATTED_DATA_PATH = Path("datasets/formatted_data.jsonl")


def generate_formatted_data() -> None:
    """
    Takes the raw data with year, inflation, income and converts it to the message prompt format gpt requires
    """
    raw_data: list[dict] = json.loads(RAW_DATA_PATH.read_text())
    training_sets: list[dict] = []
    for index, dataset in enumerate(raw_data):
        training_sets.append(
            {
                "messages": [
                    SYSTEM_MESSAGE,
                    {
                        "role": "user",
                        "content": ", ".join(
                            f"{key}: {dataset[key]}" for key in INPUT_FIELDS
                        ),
                    },
                    {
                        "role": "assistant",
                        "content": ", ".join(
                            f"{key}: {dataset[key]}" for key in OUTPUT_FIELDS
                        ),
                    },
                ]
            }
        )
    with jsonlines.open(FORMATTED_DATA_PATH, mode="w") as writer:
        writer.write_all(training_sets)


generate_formatted_data()
