# 29. Write a Python program to check whether all items are identical in a given array.
# Sample Output:
# Original array:
# [10, 20, 30, 40, 10, 10, 20]
# If all items are identical?
# false
# Original array:
# [10, 10, 10]
# If all items are identical?
# true

original = [10, 11, 10]


def all_identical(array):
    check = None
    for item in array:
        if item != array[-1]:
            check = False
        else:
            check = True
    print(check)
# or
#     check_array = True if len(set(array)) == 1 else False
#     print(check_array)


all_identical(original)
