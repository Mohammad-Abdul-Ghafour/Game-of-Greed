from  game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self,roller = None):
        self.roller = roller

    def play(self):
        print("Welcome to Game of Greed")
        wanna_paly = input("Wanna play? ")
        if wanna_paly == "n":
            print("OK. Maybe another time")
        else:
            print("Starting round 1")
            print("Rolling 6 dice...")
            roll_dice = self.roller(6)
            nums = [str(x) for x in roll_dice]
            print(','.join(nums))
            decision = input('Enter dice to keep (no spaces), or (q)uit: ')
            dice_to_keep_array = []

            for i in decision:
                dice_to_keep_array.append(int(i))

            dice_to_keep = tuple(dice_to_keep_array)
            score = GameLogic.calculate_score(dice_to_keep)
            banker = Banker()
            banker.shelf(score)
            shelved_score = banker.shelved

            dice_left = 6 - len(dice_to_keep_array)
            print(f"You have {shelved_score} unbanked points and {dice_left} dice remaining")
            print('Thanks for playing. You earned 0 points')


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()

