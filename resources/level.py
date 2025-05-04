from random import randint
from random import sample

class Level:
    
    bound_a = 10
    bound_b = 20
    finish = 30
    
    monster_list = []
    monster_map = []
    stage_map = []
    map = []

    
    def boundbuild(self):
        """
        Random the level bound and finish point.

        This function need no argumenets.

        Level_a: set by default at block 10, but randomly set the bound from block 7 - 13
        Level_b: set by default at block 20, but randomly set the bound from block a + 7 to a + 13
        Finish point: set by default at block 30, but randomly set the bound from block b + 7 to b + 13
        """

        self.bound_a = randint(7,13)
        self.bound_b = randint(self.bound_a + 7,self.bound_a + 13)
        self.finish = randint(self.bound_b + 7, self.bound_b + 13)

        for i in range(self.finish):
            if i < self.bound_a:
                self.stage_map.append('Town')
            elif i < self.bound_b:
                self.stage_map.append('Forest')
            else:
                self.stage_map.append('Castle')

    
    def boundcall(self):
        """
        This function is used to call for the result of the boundbuild that we make before.
        """
        print(f"Level B begins at block: {self.bound_a}")
        print(f"Level C begins at block: {self.bound_b}")
        print(f"This game finishes at block: {self.finish - 1}")

    
    def monster(self, num_monster_a=2, num_monster_b=3, num_monster_c=4):
        """
        To place the monster into the level through sampling.

        Arguments used:
        num_monster_a (integer, default=2): the number of monster supposed to be spawned in level A
        num_monster_b (integer, default=3): the number of monster supposed to be spawned in level B
        num_monster_c (integer, default=4): the number of monster supposed to be spawned in level C
        """

        self.monster_list.extend(sample(range(1, self.bound_a), k=min(num_monster_a,len(range(1, self.bound_a)))))
        self.monster_list.extend(sample(range(self.bound_a,self.bound_b), k=min(num_monster_b,len(range(self.bound_a,self.bound_b)))))
        self.monster_list.extend(sample(range(self.bound_b,self.finish-1), k=min(num_monster_c,len(range(self.bound_b,self.finish-1)))))

        self.monster_list.sort()

        empty_map = list(range(self.finish))
        self.monster_map = [item in self.monster_list for item in empty_map]       

    
    def mapdict(self):
        """
        This function builds up the dictionar of maps.
        which each part of dictionary consisted of the following attributes:
            block (integer): # of block in enrire game map
            stage (Strings): stage in the map (town, forest, castle)
            monster (Boolean): True if the monster is deployed in the map.
        """
        for i in range(self.finish):
            self.map.append({'block': i,
                             'stage': self.stage_map[i],
                             'monster': self.monster_map[i]})
            