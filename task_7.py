# 7. Write a Python program to check two given arrays of integers and test if they have
# the same first element or they have the same last element. Both arrays length must be 1 or more.
# Sample Output:
# true
# false
# true

given_array_1 = [1, 2, 3, 4]
given_array_2 = [4]


def check_first_last(array1, array2):
    if len(array1) >= 1 and len(array2) >= 1:
        if array1[0] == array2[0] or array1[-1] == array2[-1]:
            return True
        else:
            return False
    else:
        print('Both arrays length must be 1 or more')


print(check_first_last(given_array_1, given_array_2))
