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
    print(f"Search items start with '{start}':\n", matches)


start_with(original, start='b')
