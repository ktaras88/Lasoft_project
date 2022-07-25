# 12. Write a Python program to find the larger between the first
# and last elements of a given array of integers and length 3.
# Replace all the other values to be that value. Return the changed array.

given_array = [1, 8, 3]


def larger_and_replace(array):
    print(array)

    max_element = max(array[0], array[-1])
    print([max_element]*3)
# or
    # if array[0] > array[-1]:
    #     print([array[0]]*3)
    # else:
    #     print([array[-1]]*3)


larger_and_replace(given_array)
