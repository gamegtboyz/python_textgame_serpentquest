import random

class Monster:
    
    #bound_a = Level.bound
    
    def placement(self, bound_a, bound_b, finish, num_monster_a=2, num_monster_b=3, num_monster_c=4):
        """
        To place the monster into the level through sampling.

        Arguments used
        bound_a (integer): the block which the level shifts from map A to map B
        bounb_b (integer): the block which the level shifts from map B to map C
        finish (integer): the block which is the finish block, then the game ends
        
        num_monster_a (integer, default=2): the number of monster supposed to be spawned in level A
        num_monster_b (integer, default=3): the number of monster supposed to be spawned in level B
        num_monster_c (integer, default=4): the number of monster supposed to be spawned in level C
        """
        self.monster_list = []

        #random.sample(range(), k=)
            
