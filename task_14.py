# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.

given_array = [5, 5]


def check_twice(array):
    if array == [3, 3]:
        return 3
    elif array == [5, 5]:
        return 5


print(check_twice(given_array))
