from routers.comics import comics
from fastapi import FastAPI, status

app = FastAPI(
    title='Marvel-API',
    description='These endpoints offer a easier way to interact with marvel information',
    version='1.0'
)

origins = ["*"]

# ROUTERS
app.include_router(comics.router)
# app.include_router(duplicated.router)
    
@app.get("/", status_code=status.HTTP_200_OK) 
async def get_user(): 
    return {"message": "Welcome to Marvel-Store", "CI/CD": "Successfully deployed from pipeline"}