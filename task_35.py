# 35. Convert the array so that the first go all negative elements,
# and then positive (0 is considered as positive)

given_array = [0, 10, -1, -66, 24, 3, -3]


def negative_positive(array):
    negative = []
    positive = []
    [negative.append(item) for item in array if item < 0]
    [positive.append(item) for item in array if item >= 0]
    return negative+positive
# or
    # return sorted(array)


print(negative_positive(given_array))
