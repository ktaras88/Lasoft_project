# 13. Write a Python program to concatenate an array of arrays into one.

given_array = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


def concatenate(array):
    concatenate_list = []
    for i in array:
        for x in i:
            concatenate_list.append(x)
    print(concatenate_list)


concatenate(given_array)
