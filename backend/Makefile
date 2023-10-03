PROJECT_FOLDER="backend"

lint: autoflake isort format mypy pylint flake8 pytype

isort:
	poetry run isort .

pylint:
	poetry run pylint --reports=n --output-format=colorized --rcfile=.pylintrc -j 0 "./$(PROJECT_FOLDER)"

flake8:
	poetry run flake8 --count

autoflake:
	poetry run autoflake -r . --in-place --remove-all-unused-imports

format:
	poetry run black --exclude "\.pytype" .

build:
	poetry update

run:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
