# Marvel - Microservices

project focused on managing users through microservices, connecting favorite Marvel comics according to each user registered in the app

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


# CI/CD 
This repository has been configured with CI/CD, to automate testing process. The pipeline is configured in the next file
[CI/CD](https://github.com/Aaronga19/comics-api/blob/main/.github/workflows/build_docker_testing.yml)

The evidence of the execution, you will find at [GitHub-Actions](https://github.com/Aaronga19/comics-api/actions). Then select the last action in main branch. There, you'll see: 

<img src="https://user-images.githubusercontent.com/66045880/185210194-56c2afeb-8768-4d57-a355-5d2cfd0f0485.png" width="900" height="500">

Now, you have to select a job.

<img src="https://user-images.githubusercontent.com/66045880/185196372-953c0bce-dc0c-436b-b2b7-ce1eca26e24d.png" width="300" height="400">

So, in the step number 7, there will be an execution called _Running tests!_. 

<img src="https://user-images.githubusercontent.com/66045880/185196529-d80339db-bf29-4b15-83c0-ab4050cf5008.png" width="300" height="400">

<img src="https://user-images.githubusercontent.com/66045880/185196569-6519d6fa-7049-4738-b6f5-f37a7d0bd6dd.png" width="300" height="400">

As you can see, these tests have been executed succesfully.
