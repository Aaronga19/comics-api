# Marvel - Microservices

Project focused in order to manage users and through microservices connect favorite commics according to each user registered in the app
# CI/CD 
This repository has been configured with CI/CD, to automate testing process. The pipeline is configured in the next file
[CI/CD](https://github.com/Aaronga19/comics-api/blob/main/.github/workflows/build_docker_testing.yml)

The evidence of the execution, you will find at [GitHub-Actions](https://github.com/Aaronga19/comics-api/actions). The select the last action in main branch. There, you'll see:   Now, you have to select a job, so, in the step number 7, there is a execution called _Running tests!_. As you can see, these tests have been executed succesfully.



# Endpoints

## Marvel Microservice
___pulling container___

```bash
docker pull aaronga19/marvel-api
```
___running container___

```bash
docker run -it -p 8000:8000 aaronga19/marvel-api
```

___URL MARVEL-API Hosting___ 

> Swagger UI
> 
>> [Marvel-API (Cloud Run)](https://marvel-api-pcht5l53xa-uc.a.run.app/docs) 

## Users Microservice

___execute container___

```bash
docker pull aaronga19/user-marvel-api
```

___running container___
```bash
docker run -it -p 8001:8001 aaronga19/user-marvel-api
```

___URL USERS-MARVEL-API Hosting___

> Swagger UI
> 
> > [Users-Marvel Microservice (App Engine)](https://users-marvel-service-dot-deft-falcon-352618.uc.r.appspot.com/docs)