.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

pre-requirements:
	@scripts/pre-requirements.sh

.PHONY: local-setup
local-setup: pre-requirements ## Set up the local environment (e.g. install git hooks)
	scripts/local-setup.sh
	make install

.PHONY: install
install: pre-requirements ## Install app packages
	uv python install 3.12.8
	uv python pin 3.12.8
	uv sync

.PHONY: update
update: pre-requirements ## Updates app packages
	uv lock --upgrade

.PHONY: add-package
add-package: pre-requirements ## Install a new package in the app. ex: make add-package package=XXX
	uv add $(package)

.PHONY: remove-package
remove-package: pre-requirements ## Remove a package from the app. ex: make remove-package package=XXX
	uv remove $(package)

.PHONY: run
run: pre-requirements ## Run the app in production mode
	uv run fastapi run

.PHONY: check-typing
check-typing: pre-requirements  ## Run a static analyzer over the code to find issues
	uv run mypy .

.PHONY: check-lint
check-lint: pre-requirements ## Check code style
	uv run ruff check

.PHONY: check-format
check-format: pre-requirements  ## Check python code format
	uv run ruff format --check

checks: check-typing check-lint check-format ## Run all checks

.PHONY: lint
lint: pre-requirements ## Lint python code
	uv run ruff check --fix

.PHONY: format
format: pre-requirements  ## Format python code
	uv run ruff format

.PHONY: test
test:  ## Run tests
	uv run pytest tests -x -ra

.PHONY: pre-commit
pre-commit: pre-requirements check-lint check-format check-typing test
