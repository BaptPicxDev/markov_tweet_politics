SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: build-venv ## Create virtual environment and install requirements (local dev)
build-venv:
	echo "Creating python3 virtual environment with poetry"
	poetry config virtualenvs.in-project true
	if [ ! -f pyproject.tml ]; then
		echo "Generating pyproject.toml file."
		poetry init -n
	fi
	make add-production-packages
	make add-dev-packages
	make check-dependencies

.PHONY: add-production-packages ## Add production package to pyproject.toml (from pypi.org) using poetry
add-production-packages:
	echo "Adding production packages"
	poetry add pandas
	poetry add numpy
	poetry add markovchain
	poetry add kaggle
	poetry add fastapi
	poetry add uvicorn

.PHONY: add-dev-packages ## Add dev package to pyproject.toml(from pypi.org) using poetry
add-dev-packages:
	echo "Installing dev packages"
	poetry add --group dev pytest
	poetry add --group dev pytest-cov
	poetry add --group dev pytest-mock
	poetry add --group dev pylint

.PHONY: check-dependencies ## Ensure that all dependencies are installed
check-dependencies:
	echo "Ensure dependencies are installed"
	poetry check

.PHONY: run-pytest ## Run pytest using pytest
run-pytest:
	echo "Running pytest"
	poetry run pytest -vv --cov=src/ tests/

.PHONY: run ## Run main.py with production
run:
	poetry run python3 main.py

.PHONY: run-dev ## Run main.py with development
run-dev:
	poetry run python3 main.py --dev

.PHONY: get-dataset ## Recover dataset from kaggle
get-dataset:
	mkdir -p data/
	if [ -f "data/jacques-chirac-quotes.zip" ]; then
		echo "Removing data/jacques-chirac-quotes.zip file"
		rm data/jacques-chirac-quotes.zip
	fi
	poetry run kaggle datasets download -d niscreed/jacques-chirac-quotes
	mv jacques-chirac-quotes.zip data/jacques-chirac-quotes.zip
	cd data
	unzip -o jacques-chirac-quotes.zip

.PHONY: build-old
build-old: ## Build using docker
	make generate_requirements
	sudo docker build -t docker_old -f deploy/Dockerfile .

.PHONY: build
build: ## Build using docker-compose
	make generate_requirements
	cp .env deploy/
	sudo docker-compose -p this_is_a_test -f deploy/docker-compose.yml up -d --build
	rm deploy/.env

.PHONY: stop
stop: ## Stop and remove docker container
	sudo docker-compose -p this_is_a_test -f deploy/docker-compose.yml down

.PHONY: logs
logs: ## Show logs
	sudo docker logs -f my_app

.PHONY: clean-venv ## Clean virtual environment (local dev)
clean-venv:
	echo "Removing python3 virtual environment using poetry"

.PHONY: clean_docker_images ## Clean docker images
clean_docker_images:
	sudo docker images -a | awk '{print $3}' | xargs sudo docker rmi

.PHONY: clean_docker_containers ## Clean docker containers
clean_docker_containers:
	sudo docker ps -a | awk '{print $14}' | xargs sudo docker rm

.PHONY: generate_requirements ## Generate requirements
generate_requirements:
	echo "Generating requirements.txt file"
	poetry export -f requirements.txt --without-hashes --without-urls > requirements.txt
