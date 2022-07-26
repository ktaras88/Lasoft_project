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
