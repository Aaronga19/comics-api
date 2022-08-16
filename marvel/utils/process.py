from time import sleep
import json
from marvel import Marvel


def character_features(character:json)->tuple:
    """_summary_

    Args:
        character (json): Information about the character given in the endpoint

    Returns:
        tuple: Data filtered according to the character given
    """
    character_id = character['id']
    name = character['name']
    image = f"{character['thumbnail']['path']}.{character['thumbnail']['extension']}"
    times_in_comics = character['comics']['available']
    times_in_series = character['series']['available']
    times_in_stories = character['stories']['available']
    times_in_events = character['events']['available']
    total_times = times_in_comics + times_in_series + times_in_stories + times_in_events
    appearances = {
        'comics': times_in_comics, 
        'series':times_in_series, 
        'stories':times_in_stories,
        'events':times_in_events,
        'total': total_times
            }

    return character_id, name, image, appearances

def comics_features(comic:json)->tuple:
    """_summary_

    Args:
        character (json): Information about the character given in the endpoint

    Returns:
        tuple: Data filtered according to the character given
    """
    comic_id = comic['id']
    title = comic['title']     
    on_sale_sate = comic['dates'][0]['date']
    if len(comic['images']) != 0:
        images = comic['images']
    else: 
        images = 'Not images available'

    return comic_id, title, images, on_sale_sate

def get_all_characters(characters:Marvel)->list:
    print('Obtaining characters')
    total_len_characters = characters.all()['data']['total']
    total_characters = []
    offset= 0
    while offset <= total_len_characters:
        print(offset)
        characters_iter = characters.all(limit=100,offset=offset)['data']['results']
        for character in characters_iter:
            character_id, name, image, appearances = character_features(character)
            character_processed = {'id': character_id, 'name': name, 'image':image, 'appearances':appearances}
            total_characters.append(character_processed)
        offset += 100
        sleep(0.5)
    print('characters: ',len(total_characters))
    return total_characters

def get_all_comics(comics:Marvel)->list:
    print('Obtaining comics')
    total_len_comics = comics.all()['data']['total']
    total_comics = []
    offset= 0
    while offset <= total_len_comics:
        print(offset)
        comics_iter = comics.all(limit=100,offset=offset)['data']['results']
        for comic in comics_iter:
            comic_id, title, images, on_sale_sate = comics_features(comic)
            comic_processed = {'id': comic_id, 'name': title, 'image':images, 'onsaleDate':on_sale_sate}
            total_comics.append(comic_processed)
        offset += 100
        sleep(0.5)
    print('comics: ',len(total_comics))
    return total_comics