from resources.monster import Monster
from resources.character import Character
from resources.dice import *

class Fight:
    
    def __init__(self, your_hp, monster_hp):
        self.your_hp = your_hp
        self.monster_hp = monster_hp

    def fight(self):
        while(self.your_hp > 0 and self.monster_hp > 0):
            print(f"Your HP = {self.your_hp} | Monster's HP = {self.monster_hp}")
            fight_command = input("Please roll the dice to encounter the monster:")
            if fight_command == 'roll':
                your_dice = roll()
                monster_dice = roll()

                print(f"Your roll = {your_dice} | Monster roll = {monster_dice}")

                if(your_dice > monster_dice): self.monster_hp -= 1
                if(your_dice > monster_dice): self.your_hp -= 1
                if(your_dice == monster_dice): print("We're tie this time.")

        if self.your_hp == 0:
            print("You can't make it this time.")
        
        if self.monster_hp == 0:
            print("The monster has been defeated.")
            