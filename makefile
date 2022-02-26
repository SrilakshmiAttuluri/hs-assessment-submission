dockercompose:
	@docker-compose up
dockercomposedown:
	@docker-compose down
helmdb: 
	@helm install hs-app-db hs-app-db/ -f hs-app-db/values.yaml
helmapp:
	@helm install hs-app hs-app/ -f hs-app/values.yaml
helmdbuninstall:
	@helm uninstall hs-app-db
helmappuninstall:
	@helm uninstall hs-app

