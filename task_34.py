# 34. Compress the array, and remove all 0 from it and fill in the elements
# on the right side of the last 0 with the values-1.

given_array = [2, 7, 0, 22, 33, 0, 0, 5, 9]


def compress(array):
    compress_array = []
    index_last_0 = array[::-1].index(0)

    if index_last_0:
        for i in range(1, len(array[-index_last_0:])+1):
            array[-i] = -1

    for item in array:
        if item != 0:
            compress_array.append(item)
    print(compress_array)


compress(given_array)
