# 24. Write a Python program to check whether a given array contains
# a 3 next to a 3 or a 5 next to a 5, but not both.

given_array = [3, 1, 3, 3, 7, 5, 5]


def check_35(array):
    for i in range(1, len(array)):
        if array[i-1] == 3 and array[i] == 3 or array[i-1] == 5 and array[i] == 5:
            print('Match')


check_35(given_array)
