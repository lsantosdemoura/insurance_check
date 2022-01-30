.PHONY=help

help: ## show help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

clean: ## Remove cache files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

_base_pip:
	@pip install -U pip poetry


dev-dependencies: _base_pip ## Install development dependencies
	@poetry install

dependencies: _base_pip ## Install dependencies
	@poetry install --no-dev


# LINT
_flake8:
	@flake8 --show-source

_isort:
	@isort --diff --check-only src/

_black:
	@black --check src/

_isort-fix:
	@isort src/

_black_fix:
	@black src/


lint: _flake8 _isort _black ## Run code lint
format-code: _isort-fix _black_fix ## Format code



# TESTS

test: clean ## Run tests
	@pytest src/

test-coverage: clean ## Run tests with code coverage
	@pytest src/ --cov src/ --cov-report


# API

run-api: ## Runs the API
	@uvicorn src.main:app --reload
