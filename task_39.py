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
