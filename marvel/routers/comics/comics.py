from unicodedata import name
from fastapi.routing import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi import status, Response, HTTPException
import json
import requests

import sys 
sys.path.append('../../')
from config.marvel_api import characters
from utils.process import character_features

router = APIRouter(
    prefix="/searchComics",
    tags=['Comics']
)

@router.get("/", status_code= status.HTTP_200_OK)
async def get_all_home()->list:
    """Show all items that are registered in Marvel API

    Returns:
        list: Array dividev by each comic and character
    """
    all_characters = characters.all()['data']['results']
    all_characters = jsonable_encoder(all_characters)
    return all_characters


@router.get("/{keyword}", status_code= status.HTTP_200_OK)
async def get_one_from_keyword(keyword:str)->json:
    try:
        my_character = characters.all(name=keyword)['data']['results'][0]
        character_id, name, image, appearances = character_features(my_character)
        character = {'id': character_id, 'name': name, 'image':image, 'appearances':appearances}
        character = jsonable_encoder(character)
    except Exception: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'''Information not detected in Marvel-Api''')

    return character

@router.get("/users/{id}", status_code= status.HTTP_200_OK)
async def get_from_user(id:int)->json:
    try:
        response = requests.get('http://127.0.0.1:8001/users/')
        data = response.json()
    except Exception as err:
        print(f"It can't connect with local host.\n Connecting with server 0.0.0.0\nERROR:{err}")
        response = requests.get('http://0.0.0.0:8001/users/')
        data = response.json()
    return {'message': f'Info from: {id}', 'Data': f'{data["message"]}'}