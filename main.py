import pandas as pd

from resources.dice import roll
from resources.level import Level
from resources.character import Character
from resources.monster import Monster
from resources.fight import Fight

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
    roam_command = input("Please 'roll' the dice to walk:")
    try:
        # hear the command to roll the dice
        if(roam_command == 'roll'):
            dice = roll()
            you.position = min(you.position + dice, map.finish - 1)
            print(f"Your current position is: {you.position}")
            
        
        # this block is fight mode
        if(map.map[you.position]['monster'] == True):
            monster = Monster()
            fight_sandbox = Fight(your_hp = you.hp, monster_hp = monster.hp)
            fight_or_flee = input("Here you found the monster. Do you want to 'fight' or 'flee'?")
            
            if fight_or_flee == 'flee':
                you.hp = fight_sandbox.flee()                

            if fight_or_flee == 'fight':            
                you.hp = fight_sandbox.fight()            
        
        # this block shows when the game ends.
        if(you.position == map.finish-1):
            print(f"The quest is finally reach its end. Well done, {you.name}.")
            break

    except:
        print("Something unexpected happends. Please enter 'roll' in your console to roll the dice.")

# This block shows when you can't make it.
if you.hp <= 0:
    print("You can't make it this time. Maybe later.")