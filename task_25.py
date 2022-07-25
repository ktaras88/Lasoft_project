# 25. Write a Python program to check whether a given array of integers contains two 6's next to each other,
# or there are two 6's separated by one element, such as [6, 2, 6].

given_array = [6, 2, 6]


def check_6(array):
    i = 0
    while i < len(array):
        if array[i] == 6 and i < len(array) - 1:
            if array[i+1] == 6:
                print('Match')
            elif i < len(array) - 2 and array[i+2] == 6:
                print('Match')
        i += 1


check_6(given_array)
