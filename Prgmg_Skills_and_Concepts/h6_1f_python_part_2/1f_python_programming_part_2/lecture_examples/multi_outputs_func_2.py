

import random

def generate_three_unique_random_integers(low, high):
    number_1 = random.randint(low, high)

    while True:
        number_2 = random.randint(low, high)
        if number_2 != number_1:
            break

    while True:
        number_3 = random.randint(low, high)
        if number_3 != number_1 and number_3 != number_2:
            break
        
    returned_list = [number_1, number_2, number_3]
    return returned_list

returned_list = generate_three_unique_random_integers(1, 10)

print (returned_list[0])
print (returned_list[1])
print (returned_list[2])

