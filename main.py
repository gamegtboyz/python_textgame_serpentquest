import pandas as pd

from resources.dice import roll
from resources.level import Level
from resources.character import Character

# Set up the character's info

name = input('Before the journey begins, please let me know how are you called: ')
you = Character(name)
print(f"Oh, hi there, {you.name}. We are waiting for you for so long. Let our journey begins.")

# Build up the map object
map = Level()

map.boundbuild()    # set the game and stage length
map.monster()       # spawn the monster
map.mapdict()       # build up the map
print(pd.DataFrame(map.map))

# Start the game
print("You're at the block 0, which is basically your home.")

while(you.hp > 0):
    command_text = input("Please 'roll' the dice to start your journey:")
    try:
        if(command_text == 'roll'):
            dice = roll()
            you.position += dice
            print(f"Your current position is: {min(you.position, map.finish)}")
        
        if(you.position >= map.finish):
            print(f"The quest is finally reach its end. Well done, {you.name}")
            break

    except:
        print("Something unexpected happends. Please enter 'roll' in your console to roll the dice.")

    