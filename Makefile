install:
		poetry install

build:
		poetry build

package-install:
		python3 -m pip install --user dist/*.whl

package-force-reinstall:
		python3 -m pip install --user --force-reinstall dist/*whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml