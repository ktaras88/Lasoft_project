# 3. Write a Python program to pick a number of random elements from a given array.
# Sample Output:
# Original array:
# [12, 34, 23, 56]
#  2 random elements from the array.
# [34, 12]
#  3 random elements from the array.
# [56, 12, 34]
import random

original = [12, 34, 23, 56]


def pick_random_elements(array, amount):
    random_elements = []
    for i in range(amount):
        random_num = random.randint(0, len(array)-1)
        random_elements.append(array[random_num])
    return random_elements


print(pick_random_elements(original, 2))
