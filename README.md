# hs-assessment-submission

app.py: Is a flask webapp in python and docker-compose.yml consists both db and app service and app depends on db

About Application
app.py: Is a flask webapp in python and docker-compose.yml consists both db and app service and app depends on db and connection db using connection pooling

Commands use: 

### docker build image
```
make build
```

### local environment up 
```
make up
```

### local environemnt shutdown using docker-compose
```
make down
```

## helm deployment 
```
make install
```

## helm uninstall
```
make uninstall
```

Output:

1) http://localhost:4444/ - Welcome page
2) http://localhost:4444/healthz - Health page
3) http://localhost:4444/login - database connection page