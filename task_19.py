# 19. Write a Python program to compute the average values of a given array of except the largest and smallest values. 

given_array = [1, 2, 3, 4, 5, 6]


def average_values(array):
    max_value = max(array)
    min_value = min(array)
    sum_value = 0
    for element in array:
        sum_value += element
    print((sum_value - max_value - min_value) / (len(array)-2))


average_values(given_array)
