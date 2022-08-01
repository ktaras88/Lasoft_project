# 15. Write a Python program to find the largest odd value from a given array.

given_array = [2, 55, 81, 46, 7, 18, 1]


def largest_odd_value(array):
    odd_list = [item for item in array if item % 2 == 1]
    return max(odd_list)


print(largest_odd_value(given_array))
