from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRouter
from fastapi.security.api_key import APIKey
from fastapi import status, HTTPException, Depends
from datetime import datetime
import json

from utils import password
from models import schemas
from connection.mongdb import users_collection
from utils.dates import age
from utils.oauth2 import create_access_token
from utils.password import verify
from utils.api_key import get_api_key

router = APIRouter(
    prefix="/users",
    tags=['Comics']
)

@router.get("/", status_code= status.HTTP_200_OK)
async def get_all_home(api_key:APIKey = Depends(get_api_key))->json:
    user_list = []
    users = users_collection.find({})
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return user_list


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, api_key:APIKey = Depends(get_api_key))->json:
    # HASH the password
    hashed_password = password.hash_password(user.password)
    user.password = hashed_password
    user.birthdate = datetime.strptime(user.birthdate, '%Y-%m-%d')
    users_collection.insert_one(jsonable_encoder(user)) 
    return {'message':'user created succesfully'}

@router.post("/login", status_code= status.HTTP_200_OK)
async def user_login(user:schemas.GetUser, api_key:APIKey = Depends(get_api_key))->json:

    user_found = users_collection.find_one({"email":user.email})
    if user_found != None:
       
        if verify(user.password,user_found['password']):
            user_found['_id'] = str(user_found['_id'])
            date_of_birth = datetime.strptime(user_found['birthdate'], '%Y-%m-%dT%H:%M:%S')
            user_found['age'] = age(date_of_birth)  
            user_found.pop('birthdate')
            token = create_access_token(user_found)
            user_found['token'] = token
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password, verify your data')
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Email does not match with any user')
    
    return user_found


@router.get("/secure_endpoint")
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = "What a cool funciton"
    return {'message': response}