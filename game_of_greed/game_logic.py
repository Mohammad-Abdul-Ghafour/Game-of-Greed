import random
import collections

class GameLogic:
    def __init__(self):
        pass

    def roll_dice(value):
        i = 1
        values=[]
        while i <= value:
            values.append(random.randint(1,6))
            i += 1
        return tuple(values)

    def calculate_score(value):
        counter = collections.Counter(value)
        total = 0
        for i in counter:
            print(counter[i])
            if i == 1:
                if counter[i] == 1:
                    total += 100
                if counter[i] == 2:
                    total += 200
                if counter[i] >= 3:
                    total = 1000 * (counter[i] - 2)
        return total



if __name__ == "__main__":
    value = (1,1,1,5,5,5)
    counter = collections.Counter(value)
    total = 0
    for i in counter:
        print(counter[i])
        if i == 1:
            if counter[i] == 1:
                total += 100
            if counter[i] == 2:
                total += 200
            if counter[i] >= 3:
                total += 1000 * (counter[i] - 2)
            # if counter[i] == 3:
            #     total += 1000
            # if counter[i] == 4:
            #     total += 2000
            # if counter[i] == 5:
            #     total += 3000
            # if counter[i] == 6:
            #     total += 4000
        


# collections.Counter(value)

# Counter({'1': 3, '2': 2, '3': 1})

# tuple()
