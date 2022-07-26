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
