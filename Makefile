# Variables
PY ?= python
APP ?= main:app
HOST ?= 0.0.0.0
PORT ?= 8080
#TESTS ?= tests

.PHONY: run test format lint typecheck check

# Run FastAPI (uvicorn)
run:
	$(PY) -m uvicorn $(APP) --reload --host $(HOST) --port $(PORT)

# Run tests (pytest + coverage)
test:
	$(PY) -m pytest -q --maxfail=1 --cov=. --cov-report=term-missing $(TESTS)

# Format code (black)
format:
	$(PY) -m black .

# Lint (flake8)
lint:
	$(PY) -m flake8

# Type check (mypy)
typecheck:
	$(PY) -m mypy .

# Lint + Type check
check: lint typecheck