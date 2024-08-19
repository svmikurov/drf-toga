COMPOSE := docker compose
DRF_APP := @$(COMPOSE) exec drf-project
MANAGE := @$(DRF_APP) python manage.py


# Django

makemigrations:
	@$(MANAGE) makemigrations

dry-run:
	@$(MANAGE) makemigrations --dry-run

migrate:
	@$(MANAGE) migrate

# Docker
build:
	@$(COMPOSE) build

up:
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down

rebuild: down build up

rebuild-drf-project:
	@$(COMPOSE) down drf-project && \
	$(COMPOSE) build drf-project && \
	$(COMPOSE) up drf-project -d

# Linter
ruff:
	ruff check && ruff format --diff