from typing import Counter
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

import collections
class Game:
    def __init__(self, roller=None):
        self.roller = roller


    def cheater(self, t1, t2, nums):
        dic1 = collections.Counter(t1)
        dic2 = collections.Counter(t2)

        for item in dic2:
            if dic1[item]:
                if dic2[item] > dic1[item]:
                    print('Cheater!!! Or possibly made a typo...')
                    # print(','.join(nums))
                    return True

        return False

    

    def play(self):
        print("Welcome to Game of Greed")

        wanna_paly = input("Wanna play? ")

        if wanna_paly == "n":

            print("OK. Maybe another time")

        else:

            counter = 1
            decision = ""
            choice_input=""
            banker = Banker()
            dice_left = 6
            cheater = False

            while decision != "q":

                if choice_input != "r" and cheater == False:
                    dice_left = 6
                    print(f"Starting round {counter}")

                if cheater == False:
                    print(f"Rolling {dice_left} dice...")
                    roll_dice = self.roller(dice_left)

                ## reset cheater 
                cheater = False


                nums = [str(x) for x in roll_dice]

                print(','.join(nums))

                ################# Zilch!! ###################
                if GameLogic.calculate_score(roll_dice) == 0:
                    print ("Zilch!!! Round over")
                    print (f'You banked 0 points in round {counter}')
                    print (f"Total score is {banker.balance} points")
                    counter += 1
                    choice_input = ''
                    continue



                decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                if decision == "q":
                    if counter > 1:
                        print(f"Total score is {banker.balance} points")
                    break

                #### put the input in a tuple
                dice_to_keep_array = []
                for i in decision:
                    dice_to_keep_array.append(int(i))
                dice_to_keep = tuple(dice_to_keep_array)


                ### check if cheater!!!!!!!!
                cheater = self.cheater(roll_dice , dice_to_keep, nums)
                if cheater:
                    continue

                ###### score & shelving
                score = GameLogic.calculate_score(dice_to_keep)
                banker.shelf(score)
                shelved_score = banker.shelved
                dice_left = dice_left - len(dice_to_keep_array)
              

                print(f"You have {shelved_score} unbanked points and {dice_left} dice remaining")
                choice_input = input("(r)oll again, (b)ank your points or (q)uit ")
                
                if choice_input == "q":
                    print(f"Total score is {banker.balance} points")
                    break

                if choice_input == "b":

                    print(f"You banked {banker.shelved} points in round {counter}")

                    banker.bank()
 
                if choice_input == "r":

                    counter1 = collections.Counter(dice_to_keep)
                    # print (counter1)
                    if len(counter1) == 3 and counter1[1] == counter1[2] == counter1[3]:
                        dice_left = 6
                        continue

                    else: 
                        continue

                    

                print(f"Total score is {banker.balance} points")

                counter += 1

            print(f'Thanks for playing. You earned {banker.balance} points')


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
