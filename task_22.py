# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.

given_array = [1, 5, 2, 3, 4, 5, 6, 7, 3]


def sum_every_third(array):
    count = 0
    for element in array:
        if element == 3 or element == 5:
            count += 1
    print(f'The number of matching 3 or 5 is: {count}')


sum_every_third(given_array)
