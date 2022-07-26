# 16. Write a Python program to create a new array using the first three elements of a given array of integers.

given_array = [1, 2, 3, 4, 5, 6]


def first_three(array):
    new_array = array[:3]
    print(new_array)


first_three(given_array)
