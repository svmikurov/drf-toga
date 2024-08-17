COMPOSE := docker compose

# Docker
build:
	@$(COMPOSE) build

up:
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down

# Linter
ruff:
	ruff check && ruff format --diff