install:
	poetry install --all-extras

init:
	poetry lock --no-update
	poetry install --no-interaction --no-root --no-ansi

test:
	pytest -v -s -n 3

format:
	poetry run ruff format

lint:
	poetry run ruff check --fix .
	poetry run mypy .
