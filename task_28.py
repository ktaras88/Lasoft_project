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
