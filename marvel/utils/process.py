import json

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