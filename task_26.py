# 26. Write a Python program to check whether there is a 2 in the array
# with a 3 somewhere later in a given array of integers.

given_array = [3, 2, 1, 3, 5]


def check_23(array):
    for i in range(len(array)):
        if array[i] == 2:
            for j in range(i, len(array)):
                if array[j] == 3:
                    print(True)


check_23(given_array)
