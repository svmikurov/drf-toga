COMPOSE := docker compose

# Docker
build:
	@$(COMPOSE) build

up:
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down

rebuild: down build up

# Linter
ruff:
	ruff check && ruff format --diff