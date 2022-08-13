from marvel import Marvel
from .secrets import PUBLIC_KEY,  PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

characters = marvel.characters
comics = marvel.comics