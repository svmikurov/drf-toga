COMPOSE := docker compose

build:
	@$(COMPOSE) build

up:
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down

docker-clean:
	@$(COMPOSE) down && \
	docker image prune -a -f && \
	docker volume prune -a -f && \
	docker builder prune -a -f && \
	docker system df
