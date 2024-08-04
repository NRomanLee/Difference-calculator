.PHONY: check lint test test-coverage

check: lint test

install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
	poetry run codeclimate-test-reporter < coverage.xml
