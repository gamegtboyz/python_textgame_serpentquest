from resources.monster import Monster
from resources.character import Character
from resources.dice import *

class Fight:
    
    def __init__(self, your_hp, monster_hp):
        self.your_hp = your_hp
        self.monster_hp = monster_hp

    def fight(self):
        while(self.your_hp >= 0 or self.monster_hp >= 0):
            print(f"Your HP = {self.your_hp} | Monster's HP = {self.monster_hp}")
            fight_command = input("Please roll the dice to encounter the monster:")
            if fight_command == 'roll':
                your_dice = roll()
                monster_dice = roll()

                print(f"Your roll = {your_dice} | Monster's roll = {monster_dice}")

                if(your_dice > monster_dice): self.monster_hp -= 1
                if(your_dice < monster_dice): self.your_hp -= 1
                if(your_dice == monster_dice): print("We're tie this time.")

                if self.your_hp == 0:
                    return int(self.your_hp)
                    
                if self.monster_hp == 0:
                    print(f"The monster has been defeated. Your remaining HP = {self.your_hp}")
                    #print(type(self.your_hp))
                    return int(self.your_hp)
        
        #return int(self.your_hp)
    
    def flee(self):
        if (self.your_hp > 3):
            print(f"Your currrent HP = {self.your_hp}")
            flee_command = input('If you decide to flee, you need to sacrifice 3HP to skip this fight. Are you sure (y/n)?')
            if(flee_command == 'y'):
                self.your_hp -= 3
                return self.your_hp
            else:
                print('You decide to fight this time, alright then.')
                self.fight()

        if (self.your_hp <= 3):
            print("You're too exhausted to run. You need to fight anyway.")
            self.fight()
            
