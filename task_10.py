# 10. Write a Python program to create an array with the elements "rotated left"
# of a given array of ints length 3.
# Sample Output:
# [2, 5, 1]
# [2, 3, 1]
# [2, 4, 1]

given_array = [1, 2, 5]


def rotated_left(array):
    rotated_list = [array[1], array[2], array[0]]
    print(rotated_list)


rotated_left(given_array)
