# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.
# The script should return True for [2,3,4,5,3] or [4,3,6,7,5,7,8,5,9]. For [6,5,7,7] it should return False.

given_array = [6,5,7,7]


def check_twice(array):
    twice_3 = [item for item in array if item == 3]
    twice_5 = [item for item in array if item == 5]
    return len(twice_3) > 1 or len(twice_5) > 1


print(check_twice(given_array))
