install:
		poetry install

build:
		poetry build

package-install:
		python -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml