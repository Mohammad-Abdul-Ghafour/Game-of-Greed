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


        if len(counter) ==6 and counter[1] == counter[2] == counter[3] == counter[4] == counter[5] == counter[6]:
            total += 1500
            return total
        

        if len(counter) ==3 and counter[1] == counter[2] == counter[3]:
            total += 1500
            return total



        for i in counter:
            # print(counter[i])
            if i == 1:
                if counter[i] == 1:
                    total += 100
                if counter[i] == 2:
                    total += 200
                if counter[i] >= 3:
                    total += 1000 * (counter[i] - 2)
            if i == 2:
                if counter[i] >= 3:
                    total += 200 * (counter[i] - 2)
            if i == 3:
                if counter[i] >= 3:
                    total += 300 * (counter[i] - 2)
            if i == 4:
                if counter[i] >= 3:
                    total += 400 * (counter[i] - 2)
            if i == 5:
                if counter[i] == 1:
                    total += 50
                if counter[i] == 2:
                    total += 100
                if counter[i] >= 3:
                    total += 500 * (counter[i] - 2)
            if i == 6:
                if counter[i] >= 3:
                    total += 600 * (counter[i] - 2)
   
        

        # for 3 pairs 
        num_of_pairs = 0
        for i in counter:
            if len(counter) ==3:
                if counter[i] == 2:
                    num_of_pairs += 1
            
        if num_of_pairs == 3:
            return 1500
        ##########

        return total





























# if __name__ == "__main__":
#     value = (1,1,1,5,5,5)
#     counter = collections.Counter(value)
#     total = 0
#     for i in counter:
#         print(counter[i])
#         if i == 1:
#             if counter[i] == 1:
#                 total += 100
#             if counter[i] == 2:
#                 total += 200
#             if counter[i] >= 3:
#                 total += 1000 * (counter[i] - 2)
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
