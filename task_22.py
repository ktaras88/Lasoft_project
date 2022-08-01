# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.
# This script should return False in case array has elements different from 3 and 5.
# But not count elements. Please rewrite it.

given_array = [1, 2, 4, 6, 7, 3]


def sum_every_third(array):
    return 3 in array or 5 in array


print(sum_every_third(given_array))
