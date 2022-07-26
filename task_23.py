# 23. Write a Python program to check whether a given value appears everywhere in a given array.
# A value is "everywhere" in an array if it presents for every pair of adjacent elements in the array.

given_array = [3, 2, 5, 2, 2, 1]
given_value = 2


def check_array(array, value):
    i = 0
    while i < len(array)-1:
        if array[i] == value or array[i+1] == value:
            return True
        else:
            return False
        i += 1


print(check_array(given_array, given_value))
