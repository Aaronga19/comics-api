from fastapi.routing import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi import status, HTTPException
import json
import requests
import sys 
sys.path.append('../../')
from config.marvel_api import characters, comics
from utils.process import character_features, comics_features, get_all_characters, get_all_comics

router = APIRouter(
    prefix="/searchComics",
    tags=['Comics & Characters']
)

@router.get("/", status_code= status.HTTP_200_OK)
async def get_all_home()->dict:
    """Show all items that are registered in Marvel API.

    Returns:
        list: Array divided by each comic and character.
    """
    total_characters = get_all_characters(characters)
    # total_comics = get_all_comics(comics)
    total_comics = 'Not necessary in this endpoint'
    return {'characters': total_characters, 'comics': total_comics}


@router.get("/{keyword}", status_code= status.HTTP_200_OK)
async def get_one_from_keyword(keyword:str)->json:
    """Obtain the exact character or comic according with the argument given in the url.

    Args:
        keyword (str): Name of the character or comic.

    Raises:
        HTTPException: It couldn't find any character or comic.

    Returns:
        json: Information of the character or comic gotten by API.
    """
    try:
        my_character = characters.all(name=keyword)['data']['results'][0]
        character_id, name, image, appearances = character_features(my_character)
        character = {'id': character_id, 'name': name, 'image':image, 'appearances':appearances}
        data = jsonable_encoder(character)

    except Exception: 
        try:
            my_comic = comics.all(titleStartsWith=keyword)['data']['results'][0]
            comic_id, title, images, on_sale_sate = comics_features(my_comic)
            comic = {'id': comic_id, 'name': title, 'image':images, 'onsaleDate':on_sale_sate}
            data = jsonable_encoder(comic)

        except Exception:

            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'''Information given don't match with comics or characters in Marvel-Api''')

    return data

@router.get("/like/{keyword}", status_code= status.HTTP_200_OK)
async def get_like_keyword(keyword:str)->json:
    """Get all the characters and commics that are similar with the keyword.

    Args:
        keyword (str): Name of the character or comic (Name Starts With).

    Raises:
        HTTPException: It couldn't find any character or comic similar.

    Returns:
        json: Array with all the items that containt the keyword.
    """
    like = []
    try:
        my_characters = characters.all(nameStartsWith=keyword)['data']['results']
        for character in my_characters:
            character_id, name, image, appearances = character_features(character)
            character = {'id': character_id, 'name': name, 'image':image, 'appearances':appearances}
            like.append(character)
        my_comics = comics.all(titleStartsWith=keyword)['data']['results']
        for comic in my_comics:
            comic_id, title, images, on_sale_sate = comics_features(comic)
            comic = {'id': comic_id, 'name': title, 'image':images, 'comic':on_sale_sate}
            like.append(comic)

    except Exception: 

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'''Information given don't match with comics or characters in Marvel-Api''')

    return like

@router.get("/microservice/home", status_code= status.HTTP_200_OK)
async def get_from_user()->json:
    """Consumes users-microservice-api.

    Returns:
        json: Message from home in the microservice
    """
    try:
        response = requests.get('https://users-marvel-service-dot-deft-falcon-352618.uc.r.appspot.com')
        data = response.json()
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Troubles connecting with server in GCP\nERROR:{err}")

    return {'message': f'Request done', 'User-microservice-response': f'{data["message"]}'}