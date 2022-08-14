import unittest
import sys 
sys.path.append('..')
from config.marvel_api import characters, comics

class TestMarvelAPI(unittest.TestCase):
    characters.all()

    # def test_total_characters(self):
    #     message = 'Characters amount has changed'
    #     self.assertIn('http', link, msg=message)

    def test_get_one_character(self): 
        message = 'Get one character is not working as expected'
        thor = characters.all(name='thor')['data']['results'][0]
        self.assertEqual(thor['name'].lower(), 'thor', msg=message)
        

    # def test_droped_links(self):
    #     message = 'Links were not filtered'
    #     self.assertLessEqual(len(self.dataurl),len(self.houses_deptos), message)





if __name__ == '__main__':
    unittest.main()