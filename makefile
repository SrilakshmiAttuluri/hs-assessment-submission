.PHONY: build up down lint deploy uninstall

build:
	@docker-compose build
up:
	@docker-compose up
down:
	@docker-compose down
lint:
	@helm lint hs-app
install:
	@helm upgrade --install hs-app hs-app/ -f hs-app/values.yaml -n default
uninstall:
	@helm uninstall hs-app

