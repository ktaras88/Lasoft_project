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
