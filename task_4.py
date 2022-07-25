# 4. Write a Python program to check whether first and the last element are the same
# as a given array of integers. The array length must be 1 or more.
# Sample Output:
# false
# true
# false

given_array = [1, 2, 3, 4, 1]


def chek(array):
    if len(array) >= 1 and array[0] == array[-1]:
        print(True)
    else:
        print(False)


chek(given_array)
