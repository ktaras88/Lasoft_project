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
