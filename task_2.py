# 2. Write a Python program to check whether 7 appears as either the first or last element in a given array.
# The array length must be 1 or more.
# Sample Output:
# true
# true
# false

given_array = [1, 2, 7]


def seven_exist(array):
    if len(array) >= 1:
        if array[0] == 7 or array[-1] == 7:
            print(True)
        else:
            print(False)
    else:
        print('There is less then 1 digit')


seven_exist(given_array)
