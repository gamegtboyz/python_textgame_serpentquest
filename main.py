import pandas as pd

from resources.dice import roll
from resources.level import Level
from resources.character import Character

# Set up the character's info

name = input('Before the journey begins, please let me know how are you called: ')
character = Character(name)
print(f"Oh, hi there, {character.name}. We are waiting for you for so long. Let our journey begins.")

# This part is to build up the map object
map = Level()

map.boundbuild()
map.monster()
map.mapdict()
print(pd.DataFrame(map.map))





