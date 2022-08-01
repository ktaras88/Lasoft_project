# 21. Write a Python program to compute the sum of every third element of a given array of integers.

given_array = [1, 2, 3, 4, 5, 6, 7]


def sum_every_third(array):
    return sum(array[2::3])


print(sum_every_third(given_array))
