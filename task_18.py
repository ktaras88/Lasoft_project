# 18. Write a Python program to find the difference between the largest
# and smallest values of a given array of integers.

given_array = [1, 2, 3, 4, 5, 6, 7]


def different(array):
    return max(array) - min(array)


print(different(given_array))
