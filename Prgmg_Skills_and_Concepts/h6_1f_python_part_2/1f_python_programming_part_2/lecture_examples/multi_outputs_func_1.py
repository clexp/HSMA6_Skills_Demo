

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
        
    return number_1, number_2, number_3

num_1, num_2, num_3 = generate_three_unique_random_integers(1, 10)

print (num_1)
print (num_2)
print (num_3)

