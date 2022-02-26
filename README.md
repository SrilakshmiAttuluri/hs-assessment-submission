# hs-assessment-submission

Need python3, docker, helm, kubernetes, kubectl, make to run the application

About Application
app.py: Is a flask webapp in python and docker-compose.yml consists both db and app service and app depends on db and connection db using connection pooling

Commands use: docker-compose up

Output:

1) http://localhost:4444/ - Welcome page
2) http://localhost:4444/healthz - Health page
3) http://localhost:4444/login - database connection page

helm charts: 
1) hs-app - consists of app helm chart with version 0.0.1 - Deployment with service,hpa, resource limits, healthz check - Liveliness and readiness, configmap and secrets (app image is srilakshmiattuluri/hsassessment:latest)
2) hs-app-db - consists of mysql helm cahrt with version 0.0.1 - statefuleset with service, pv,pvc, configmap, secerts,(db image is mysql:5.7 open image)

commands:
helm install hs-app-db hs-app-db/ -f hs-app-db/values.yaml
helm install hs-app hs-app/ -f hs-app/values.yaml



