# 17. Write a Python program to get the number of even integers in a given array.

given_array = [1, 2, 3, 4, 5, 6, 7, 22]


def number_of_even(array):
    print(len([element for element in array if element % 2 == 0]))


number_of_even(given_array)
