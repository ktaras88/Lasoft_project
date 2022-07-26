# 20. Write a Python program to compute the sum of the numbers of a given array
# except for the number 17 and numbers that come immediately after a 17.

given_array = [1, 2, 3, 17, 5, 6]


def sum_array(array):
    return sum(array[:array.index(17)])


print(sum_array(given_array))
