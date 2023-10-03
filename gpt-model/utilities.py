INPUT_FIELDS = ["year", "inflation", "income"]
OUTPUT_FIELDS = ["food", "clothing", "entertainment", "transport"]

SYSTEM_MESSAGE = {
    "role": "system",
    "content": "This chatbot calculates expected household expenditure given inflation, year, and household income.",
}


def generate_prompt(**kwargs):
    return ", ".join(f"{key}: {kwargs[key]}" for key in INPUT_FIELDS)


def format_response(response: str) -> dict:
    """
    Takes the response from the api call and formats it into a dictionary
    """
    return {
        key: float(value) for key, value in zip(OUTPUT_FIELDS, response.split(", "))
    }
