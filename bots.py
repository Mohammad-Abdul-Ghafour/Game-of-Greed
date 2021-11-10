"""Place in root of Game of Greed Project,
at same level as pyproject.toml
"""

import builtins
import re
from abc import abstractmethod
import collections 


from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    @classmethod
    def play(cls, num_games=10):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Game() # doesn't pass a mock roller
            try:
               score =  game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            # mega_total += player.total_score
            mega_total +=score
            player.reset()

        print(
            f"Congrats! {num_games} games (maybe) played with average score of {mega_total // num_games}"
        )


class AmmanBot(BasePlayer):
    def __init__(self):
        super().__init__()
        self.dice_left = 6

    def _mock_print(self, *args):
        self.old_print(*args)
        printed_data = args[0]
        if printed_data[0].isdigit():
            self.rolled_dice = tuple(int(ch) for ch in printed_data.split(','))
            # '2,3,1,2,6,4' ==> (2,3,1,2,6,4)

    def _mock_input(self, *args):
        self.old_print(*args)
       
        if args[0].startswith('Wanna play'):
            return 'y'
        elif args[0].startswith('Enter dice'):
            max_score = self.calculate_max_score(self.rolled_dice)
            self.dice_left = self.dice_left - len(max_score)
            # self.old_print(self.calculate_max_score(self.rolled_dice))
            return max_score
            # self.old_print(self.rolled_dice)
            # return "".join([str(i) for i in self.rolled_dice])
            # if 1 in self.rolled_dice:
            #     return '1'
            # elif 5 in self.rolled_dice:
            #     return '5'
            # else:
            #     return 'q'
        elif self.dice_left >= 3 :
            
            return 'r'
        elif args[0].startswith('(r)oll again, (b)ank your points or (q)ui'):
            return 'b'
        else:
            return 'q'

    def calculate_max_score(self,rolled_dice):
        counter = collections.Counter(rolled_dice)
        dice = ""
        
        if len(counter) == 6 and counter[1] == counter[2] == counter[3] == counter[4] == counter[5] == counter[6]:
            dice = "123456"
            return dice
        if len(counter) == 3 and counter.most_common(2)[0][1] == 2:
            dice = "".join([str(c) for c in rolled_dice])
            return dice
        if 1 in counter :
            i = 1
            while i<= counter[1]:
                dice = dice+"1"
                i+=1
        if 5 in counter :
            i = 1
            while i<= counter[5]:
                dice = dice+"5"
                i+=1
        for j in [2,3,4,6]:
            
            if j in counter and counter[j]>=3 :
                i = 1
                while i<= counter[j]:
                    dice = dice+f"{j}"
                    i+=1 
        
             
        return dice



if __name__=="__main__":
    # bot1 = BasePlayer()
    # bot1.play()
    amman_bot = AmmanBot()
    amman_bot.play()