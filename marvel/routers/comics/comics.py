from fastapi.routing import APIRouter
from fastapi import status
import json
import requests

router = APIRouter(
    prefix="/searchComics",
    tags=['Comics']
)


@router.get("/", status_code= status.HTTP_200_OK)
async def get_all_home()->json:
    return {'message': 'Show all items'}


@router.get("/{keyword}", status_code= status.HTTP_200_OK)
async def get_one_keyword(keyword:str)->json:
    
    return {'message': f'Show items that are similar to: {keyword.capitalize()}'}

@router.get("/info/{id}", status_code= status.HTTP_200_OK)
async def get_from_user(id:int)->json:
    response = requests.get('http://127.0.0.1:8000/searchComics/thanos')
    data = response.json()
    return {'message': f'Info from: {id}', 'Data': f'{data["message"]}'}