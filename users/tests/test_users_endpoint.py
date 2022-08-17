import unittest
import requests
from secure.secrets import settings

class TestUsersAPI(unittest.TestCase):

    API_URL = 'https://users-marvel-service-dot-deft-falcon-352618.uc.r.appspot.com'

    def test_get_secure_endpoint_without_apikey(self): 
        url = f"{self.API_URL}/users/secure_endpoint"
        response = requests.get(url)
        self.assertEqual(response.status_code, 403, msg='api-key is not working working')
        
    def test_get_secure_endpoint_with_apikey(self):
        url = f"{self.API_URL}/users/secure_endpoint"
        headers = {'api-key': settings.api_key}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200, msg='Request working with api-key')

    def test_get_message_secure_endpoint(self):
        url = f"{self.API_URL}/users/secure_endpoint"
        headers = {'api-key': settings.api_key}
        response = requests.get(url, headers=headers)
        message = response.json()['message']
        self.assertEqual(message, 'What a cool funciton', msg='The message has changed')


if __name__ == '__main__':
    unittest.main()