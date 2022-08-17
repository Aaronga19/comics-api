import unittest
import sys 
sys.path.append('..')
from config.marvel_api import characters, comics
from utils.process import character_features

class TestMarvelAPI(unittest.TestCase):
    
    like = []
    my_characters = characters.all(nameStartsWith='hulk')['data']['results']
    for character in my_characters:
        character_id, name, image, appearances = character_features(character)
        character = {'id': character_id, 'name': name, 'image':image, 'appearances':appearances}
        like.append(character)

    hulk = {
        'id': 1017098,
        'name': 'Hulk (HAS)',
        'image': 'http://i.annihil.us/u/prod/marvel/i/mg/d/10/5232027069e61.jpg',
        'appearances': {
            'comics': 1,
            'series': 1,
            'stories': 1,
            'events': 0,
            'total': 3}
        }
        
    def test_get_one_character(self): 
        message = 'Get one character is not working as expected'
        thor = characters.all(name='thor')['data']['results'][0]
        self.assertEqual(thor['name'].lower(), 'thor', msg=message)
        
    def test_hulkhas_in_characters(self):
        self.assertIn(self.hulk,self.like,msg='The second item in the list, is not Hulk (HAS)')
    
    def test_len_characters_hulk(self):
        self.assertEqual(len(self.like), 9, msg='There are more or less items registered with keyword: hulk')

    def test_character_certain_position(self):
        self.assertEqual(self.hulk,self.like[1], msg='Hulk (HAS) is not already the second one in the list')
        

if __name__ == '__main__':
    unittest.main()