# 15. Write a Python program to find the largest odd value from a given array.

given_array = [2, 55, 81, 46, 7, 18, 1]


def largest_odd_value(array):
    odd_list = []
    for element in array:
        if element % 2 == 1:
            odd_list.append(element)
    print(max(odd_list))


largest_odd_value(given_array)
