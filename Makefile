install:
		poetry install

build:
		poetry build

package-install:
		python -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest