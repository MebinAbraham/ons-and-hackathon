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

mypy:
	poetry run mypy "./$(PROJECT_FOLDER)"

pytype:
	poetry run pytype --keep-going --jobs auto "./$(PROJECT_FOLDER)"

format:
	poetry run black --exclude "\.pytype" .

build:
	poetry update
