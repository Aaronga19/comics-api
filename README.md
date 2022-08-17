# Marvel - Microservices

Project focused in order to manage users and through microservices connect favorite commics according to each user registered in the app
# CI/CD 
This repository has been configured with CI/CD, to automate testing process. The pipeline is configured in the next path
[CI/CD](https://github.com/Aaronga19/comics-api/blob/main/.github/workflows/build_docker_testing.yml)

# Endpoints

## Marvel

___execute container___

```bash
docker run -it -p 8000:8000 marvel-api
```

### Uploading to Dockerhub

```bash
docker tag marvel-api:latest aaronga19/marvel-api 

docker push aaronga19/marvel-api
```
## URL MARVEL-API Serving 

> Swagger UI
> 
>> [Marvel-API (Cloud Run)](https://marvel-api-pcht5l53xa-uc.a.run.app/docs) 

## Users

___execute container___
```bash
docker run -it -p 8001:8001 aaronga19/user-marvel-api
```
### Uploading to Dockerhub

```bash
docker tag user-marvel-api:latest aaronga19/user-marvel-api

docker push aaronga19/user-marvel-api
```
## URL USERS-MARVEL-API Serving

> Swagger UI
> 
> > [Users-Marvel Microservice (App Engine)](https://users-marvel-service-dot-deft-falcon-352618.uc.r.appspot.com/docs)