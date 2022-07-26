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
