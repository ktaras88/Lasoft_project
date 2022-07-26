# 16. Write a Python program to create a new array using the first three elements of a given array of integers.

given_array = [1, 2, 3, 4, 5, 6]


def first_three(array):
    new_array = array[:3]
    return new_array


print(first_three(given_array))


# 17. Write a Python program to get the number of even integers in a given array.

given_array = [1, 2, 3, 4, 5, 6, 7, 22]


def number_of_even(array):
    return len([element for element in array if element % 2 == 0])


print(number_of_even(given_array))


# 18. Write a Python program to find the difference between the largest
# and smallest values of a given array of integers.

given_array = [1, 2, 3, 4, 5, 6, 7]


def different(array):
    return max(array) - min(array)


print(different(given_array))


# 19. Write a Python program to compute the average values of a given array of except the largest and smallest values.

given_array = [1, 2, 3, 4, 5, 6]


def average_values(array):
    max_value = max(array)
    min_value = min(array)
    sum_value = 0
    for element in array:
        sum_value += element
    return (sum_value - max_value - min_value) / (len(array)-2)


print(average_values(given_array))


# 20. Write a Python program to compute the sum of the numbers of a given array
# except for the number 17 and numbers that come immediately after a 17.

given_array = [1, 2, 3, 17, 5, 6]


def sum_array(array):
    return sum(array[:array.index(17)])


print(sum_array(given_array))


# 21. Write a Python program to compute the sum of every third element of a given array of integers.

given_array = [1, 2, 3, 4, 5, 6, 7]


def sum_every_third(array):
    return sum(array[2::3])


print(sum_every_third(given_array))


# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.

given_array = [1, 2, 4, 6, 7, 3]


def sum_every_third(array):
    return 3 in array or 5 in array


print(sum_every_third(given_array))


# 23. Write a Python program to check whether a given value appears everywhere in a given array.
# A value is "everywhere" in an array if it presents for every pair of adjacent elements in the array.

given_array = [3, 2, 5, 2, 2, 1]
given_value = 2


def check_array(array, value):
    i = 0
    while i < len(array)-1:
        if array[i] == value or array[i+1] == value:
            return True
        else:
            return False
        i += 1


print(check_array(given_array, given_value))


# 24. Write a Python program to check whether a given array contains
# a 3 next to a 3 or a 5 next to a 5, but not both.

given_array = [3, 1, 3, 3, 7, 5]


def check_35(array):
    check = None
    for i in range(1, len(array)):
        if array[i-1] == 3 and array[i] == 3 or array[i-1] == 5 and array[i] == 5:
            check = True
            break
        else:
            check = False
    return check


print(check_35(given_array))


# 25. Write a Python program to check whether a given array of integers contains two 6's next to each other,
# or there are two 6's separated by one element, such as [6, 2, 6].

given_array = [6, 2, 6]


def check_6(array):
    i = 0
    while i < len(array):
        if array[i] == 6 and i < len(array) - 1:
            if array[i+1] == 6:
                return True
            elif i < len(array) - 2 and array[i+2] == 6:
                return True
        else:
            return False
        i += 1


print(check_6(given_array))


# 26. Write a Python program to check whether there is a 2 in the array
# with a 3 somewhere later in a given array of integers.

given_array = [3, 2, 1, 3, 5]


def check_23(array):
    exist_2 = array.index(2) if 2 in array else False
    if exist_2:
        return True if 3 in array[exist_2:] else False
    return False


print(check_23(given_array))


# 27. Write a Python program to convert an array into a hash.
# Sample Output:
# Original array:
# [(10, 5), (20, 3), (30, 4), (10,2)]
# Hash:
# {10:(5,2), 20:(3), 30:(4)}

original = [(10, 5), (20, 3), (30, 4), (10, 2)]


def convert_into_hash(array):
    a_hash = {}
    for element in array:
        if element[0] not in a_hash:
            a_hash[element[0]] = element[1]
        else:
            a_hash[element[0]] = (a_hash[element[0]], element[1])
    return a_hash


print(convert_into_hash(original))


# 28. Write a Python program to find the most occurred item in a given array.
# Sample Output:
# Original array:
# [10, 20, 30, 40, 10, 10, 20]
# Frequency of numbers:
# {10: 3, 20: 2, 30: 1, 40: 1}

original = [10, 20, 30, 40, 10, 10, 20]


def most_occurred(array):
    frequency_of_numbers = {}
    for item in array:
        if item not in frequency_of_numbers:
            frequency_of_numbers[item] = 1
        else:
            frequency_of_numbers[item] += 1
    return frequency_of_numbers


print(most_occurred(original))


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

original = [10, 10, 10]


def all_identical(array):
    check = None
    for item in array:
        if item != array[-1]:
            check = False
            break
        else:
            check = True
    return check
# or
#     check_array = True if len(set(array)) == 1 else False
#     return check_array


print(all_identical(original))


# 30. Write a Python program to search items starting with a specified string of a given array.
# Sample Output:
# Original array:
# ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]
# Search items start with 'ab':
# ["abcde", "abdf", "abdgse"]
# Search items start with 'b':
# ["bdefa", "bacdef"]

import re

original = ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]


def start_with(array, start='ab'):
    string = ' '.join(array)
    template = rf'\b{start}\w*'
    matches = re.findall(template, string)
    print('Original array: \n', array)
    print(f"Search items start with '{start}':")
    return matches


print(start_with(original, start='b'))
