# 31. Write a Python program to iterate an array starting from the last element.
# Sample Output:
# Original array:
# [10, 20, 30, 40, 10, 10, 20]
# Reverse array:
# 20
# 10
# 10
# 40
# 30
# 20
# 10

original = [10, 20, 30, 40, 10, 10, 20]


def reverse_iterate(array):
    print('Original array:\n', array)
    print('Reverse array:')
    for item in array[::-1]:
        print(item)


reverse_iterate(original)


# 32. Write a Python program to iterate over the first n elements of a given array.
# Sample Output:
# Original array:
# ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]
# First 3 elements:
# ["abcde", "abdf", "adeab"]

original = ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]
n = 3


def first_three(array, n):
    print('Original array:\n', array)
    print('First 3 elements:\n', array[:n])


first_three(original, n)


# 33. Write a Python program to sort a given array of strings by length.
# Sample Output:
# Original array:
# ["abcde", "abdf", "adeab", "abdgeee", "bdefa", "abc", "ab", "a", "bacdef"]
# Sorted array of strings by length
# ["a", "ab", "abc", "abdf", "abcde", "adeab", "bdefa", "bacdef", "abdgeee"]

original = ["abcde", "abdf", "adeab", "abdgeee", "bdefa", "abc", "ab", "a", "bacdef"]


def sort_by_length(array):
    print('Original array:\n', array)
    print('Sorted array of strings by length:\n', sorted(array, key=len))


sort_by_length(original)


# 34. Compress the array, and remove all 0 from it and fill in the elements
# on the right side of the last 0 with the values-1.

given_array = [2, 7, 0, 22, 33, 0, 0, 5, 9]


def compress(array):
    compress_array = []
    index_last_0 = array[::-1].index(0)

    if index_last_0:
        for i in range(1, len(array[-index_last_0:])+1):
            array[-i] = -1

    for item in array:
        if item != 0:
            compress_array.append(item)
    print(compress_array)


compress(given_array)


# 35. Convert the array so that the first go all negative elements,
# and then positive (0 is considered as positive)

given_array = [0, 10, -1, -66, 24, 3, -3]


def negative_positive(array):
    negative = []
    positive = []
    [negative.append(item) for item in array if item < 0]
    [positive.append(item) for item in array if item >= 0]
    print(negative+positive)
# or
    # new = sorted(array)
    # print(new)


negative_positive(given_array)


# 36. Write a program which counts the number of times a number appears in an array.

given_array = [1, 2, 1, 3, 4, 5, 4, 1]


def count_the_number(array, number):
    count = 0
    for item in array:
        if item == number:
            count += 1
    print(count)


count_the_number(given_array, 1)


# 37. In a two-dimensional array of order M and N, swap the specified columns.

given_array = [[1, 2, 3], [1, 2, 3]]


def swap(array, n, m):
    for item in array:
        item[n], item[m] = item[m], item[n]
        print(item)


swap(given_array, 1, 2)


# 38. Given the single-mass array with predefined values with a size of 10 items.
# Show on the screen array, and find the values that are repeated two and more times.

given_array = [1, 2, 3, 4, 5, 5, 4, 3, 6, 7]


def repeated(array):
    print(array)
    unrepeatable = []
    for item in array:
        if item not in unrepeatable:
            unrepeatable.append(item)
        else:
            print(f'Value {item} repeated two or more times')


repeated(given_array)


# 39. Given the single-mass array with predefined values with a size of 10 items.
# Show on the screen array, and find the value that is the smallest odd number.

given_array = [1, 2, 3, -4, 5, 5, 4, -3, 6, 7]

def smallest_odd(array):
    print(array)
    odd = []
    for item in array:
        if item % 2 == 1:
            odd.append(item)
    print(min(odd))


smallest_odd(given_array)


# 40. Given the single-mass array. Cyclically shift the array on the K elements, on the right or left side

given_array = [1, 2, 3, 4, 5]
K = 1
sides = 'right'


def cyclically_shift(array, side, k):
    print(f'Given single-mass array:\n{array}')
    shifted = []
    len_shifted = 0
    for i in range(len(array)):
        if side == 'left':
            if i+k < len(array):
                shifted.append(array[i+k])
                len_shifted += 1
            else:
                shifted.append(array[i-len_shifted])
        elif side == 'right':
            if i+k < len(array):
                shifted.append(array[-k+i])
            else:
                shifted.append(array[i-k])
    print(f'Cyclically shifted:\n{shifted}')


cyclically_shift(given_array, sides, K)
