from random import randint, random

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from app.templates import templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


def predict(*, year: int, inflation: float, income: float) -> dict:
    return {
        "food": randint(0, 1000),
        "clothing": randint(0, 1000),
        "entertainment": randint(0, 1000),
        "transport": randint(0, 1000),
        "success": True,
    }


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    output_data = {"request": request}
    return templates.TemplateResponse("base.html", output_data)


@app.get("/predict")
async def _predict(
    request: Request, year: int, inflation: float, income: float
) -> dict:
    year = year or 2000
    inflation = inflation or 0
    income = income or 0

    data = predict(
        year=year,
        inflation=inflation,
        income=income,
    )

    total = sum(data.values())
    data["total"] = total
    data["year"] = year
    data["inflation"] = inflation
    data["income"] = income
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
