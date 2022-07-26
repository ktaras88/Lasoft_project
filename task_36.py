# 36. Write a program which counts the number of times a number appears in an array.

given_array = [1, 2, 1, 3, 4, 5, 4, 1]


def count_the_number(array, number):
    count = 0
    for item in array:
        if item == number:
            count += 1
    return count


print(count_the_number(given_array, 1))
