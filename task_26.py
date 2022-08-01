# 26. Write a Python program to check whether there is a 2 in the array
# with a 3 somewhere later in a given array of integers.

given_array = [3, 2, 1, 3, 5]


def check_23(array):
    exist_2 = array.index(2) if 2 in array else False
    if exist_2:
        return True if 3 in array[exist_2:] else False
    return False


print(check_23(given_array))
