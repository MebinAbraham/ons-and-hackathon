import argparse

from _decimal import Decimal

from api import predict


def calculate_future_income(income, inflation, year):
    """Implement this"""
    return income


def main():
    parser = argparse.ArgumentParser(
        description="Calculate future income based on given parameters."
    )
    parser.add_argument("income", type=Decimal, help="Current income")
    parser.add_argument(
        "inflation", type=Decimal, help="Inflation rate (as a percentage)"
    )
    parser.add_argument("year", type=int, help="Number of years in the future")
    parser.add_argument(
        "salary_increase",
        type=Decimal,
        help="Annual salary increase rate (as a percentage)",
    )

    args = parser.parse_args()

    salary_increase = args.salary_increase or 1
    # calculate income after salary increase
    income = args.income * (1 + salary_increase / 100)

    future_income = calculate_future_income(income, args.inflation, args.year)
    print(
        f"Projected income after {args.year} years: ${future_income:.2f} with {args.inflation}% inflation and {args.salary_increase}% salary increase"
    )
    expenditure = predict(
        income=future_income, inflation=args.inflation, year=args.year
    )
    print(f"Projected expenditure: {expenditure}")


if __name__ == "__main__":
    main()
