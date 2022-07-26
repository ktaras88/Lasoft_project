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
    print('First 3 elements:')
    return array[:n]


print(first_three(original, n))

