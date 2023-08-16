coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=src/* -m pytest -ra
	python -m coverage report -m

deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install black coverage mypy ruff pytest nox sphinx

lint:  ## Lint and static-check
	python -m black
	python -m ruff
	python -m mypy

test:  ## Run tests
	python -m pytest -ra

nox:   ## Run tox
	python -m nox