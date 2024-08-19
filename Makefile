COMPOSE := docker compose

# Docker
build:
	@$(COMPOSE) build

up:
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down

rebuild-drf-project:
	@$(COMPOSE) down drf-project && \
	$(COMPOSE) build drf-project && \
	$(COMPOSE) up drf-project -d

# Linter
ruff:
	ruff check && ruff format --diff