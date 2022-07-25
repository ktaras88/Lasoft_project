# 5. Write a Python program to compute the sum of elements in a given array.
# Sample Output:
# Original array:
# [12, 34, 23, 56]
# Sum of the values of the above array:
# 125

original = [12, 34, 23, 56]


def compute_sum(array):
    sum_elements = 0
    for i in array:
        sum_elements += i
    print(f'Sum of the values of the array: {sum_elements}')


compute_sum(original)

# or

# print(sum(original))
