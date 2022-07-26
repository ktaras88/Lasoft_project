# 1. Write a Python program to check if a value exists in an array.
# Sample Output:
# Original array:
# ["Red", "Green", "Blue", "White"]
# Check if 'Green' in color array!
# true
# Check gif 'Pink' in color array!
# false

original = ["Red", "Green", "Blue", "White"]
color = 'Green'

print(color in original)


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
            return True
        else:
            return False
    else:
        print('There is less then 1 digit')


print(seven_exist(given_array))


# 3. Write a Python program to pick a number of random elements from a given array.
# Sample Output:
# Original array:
# [12, 34, 23, 56]
#  2 random elements from the array.
# [34, 12]
#  3 random elements from the array.
# [56, 12, 34]
import random

original = [12, 34, 23, 56]


def pick_random_elements(array, amount):
    random_elements = []
    for i in range(amount):
        random_num = random.randint(0, len(array)-1)
        random_elements.append(array[random_num])
    return random_elements


print(pick_random_elements(original, 2))


# 4. Write a Python program to check whether first and the last element are the same
# as a given array of integers. The array length must be 1 or more.
# Sample Output:
# false
# true
# false

given_array = [1, 2, 3, 4, 1]


def chek(array):
    return len(array) >= 1 and array[0] == array[-1]


print(chek(given_array))


# 5. Write a Python program to compute the sum of elements in a given array.
# Sample Output:
# Original array:
# [12, 34, 23, 56]
# Sum of the values of the above array:
# 125

original = [12, 34, 23, 56]


def compute_sum(array):
    sum_elements = 0
    for i in array:
        sum_elements += i
    return sum_elements


print(compute_sum(original))

# or
# return sum(original)


# 6. Write a Python program to remove duplicate elements from a given array.
# Sample Output:
# Original array:
# [1, 2, 3, 4, 1, 2, 2, 3, 5, 6]
#  Array with unique elements:
# [1, 2, 3, 4, 5, 6]

original = [1, 2, 3, 4, 1, 2, 2, 3, 5, 6]


def remove_duplicate(array):
    unique_elements = []
    for element in array:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements


print(remove_duplicate(original))

# or
# unique_elements = []
# [unique_elements.append(element) for element in original if element not in unique_elements]
# return unique_elements

# or
# return set(original)


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


# 8. Write a Python program to remove blank elements from a given array.
# Sample Output:
# Original array:
# ["Red", "Green", "", "Blue", "White"]
# Remove a blank element from the above array:
# ["Red", "Green", "Blue", "White"]

original = ["Red", "Green", "", "Blue", "White"]


def remove_blank(array):
    without_blank = []
    for element in array:
        if element:
            without_blank.append(element)
    return without_blank


print(remove_blank(original))

# or
# return [element for element in original if element]


# 9. Write a Python program to split a delimited string into an array.
# Sample Output:
# Original delimited string:
# Red, Green, Blue, White1, 3, 4, 5, 7String to array:
# ["Red", " Green", " Blue", " White"]
# [1, 3, 4, 5, 7]
import re

delimited_string = 'Red, Green, Blue, White1, 3, 4, 5, 7'


def string_to_array(string):
    template_words = '[A-Z][a-z]{2,}'
    template_digit = r'\d'

    words = re.findall(template_words, string)
    digits = re.findall(template_digit, string)

    print(words)
    return list(map(int, digits))

# or

    # separable_index = string.find('1')
    # words = string[:separable_index].split(',')
    # digits = string[separable_index:].split(',')
    # print(words)
    # return [int(x) for x in digits]


print(string_to_array(delimited_string))


# 10. Write a Python program to create an array with the elements "rotated left"
# of a given array of ints length 3.
# Sample Output:
# [2, 5, 1]
# [2, 3, 1]
# [2, 4, 1]

given_array = [2, 3, 1]


def rotated_left(array):
    rotated_list = [array[1], array[2], array[0]]
    return rotated_list


print(rotated_left(given_array))


# 11. Write a Python program to create a new array with the elements in reverse order
# from a given an array of integers length 3.

given_array = [1, 2, 3]


def reverse_order(array):
    return array[::-1]


print(reverse_order(given_array))


# 12. Write a Python program to find the larger between the first
# and last elements of a given array of integers and length 3.
# Replace all the other values to be that value. Return the changed array.

given_array = [1, 8, 3]


def larger_and_replace(array):
    print(array)

    max_element = max(array[0], array[-1])
    return [max_element]*3
# or
    # if array[0] > array[-1]:
    #     print([array[0]]*3)
    # else:
    #     print([array[-1]]*3)


print(larger_and_replace(given_array))


# 13. Write a Python program to concatenate an array of arrays into one.

given_array = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


def concatenate(array):
    concatenate_list = []
    for i in array:
        for x in i:
            concatenate_list.append(x)
    return concatenate_list


print(concatenate(given_array))


# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.
# The script should return True for [2,3,4,5,3] or [4,3,6,7,5,7,8,5,9]. For [6,5,7,7] it should return False.

given_array = [6,5,7,7]


def check_twice(array):
    twice_3 = [item for item in array if item == 3]
    twice_5 = [item for item in array if item == 5]
    return len(twice_3) > 1 or len(twice_5) > 1


print(check_twice(given_array))


# 15. Write a Python program to find the largest odd value from a given array.

given_array = [2, 55, 81, 46, 7, 18, 1]


def largest_odd_value(array):
    odd_list = [item for item in array if item % 2 == 1]
    return max(odd_list)


print(largest_odd_value(given_array))
