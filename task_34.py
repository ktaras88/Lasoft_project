# 34. Compress the array, and remove all 0 from it and fill in the elements
# on the right side of the last 0 with the values-1.

given_array = [2, 0, 7, 22, 0, 0, 33, 5, 9]


def compress(array):
    compress_array = []
    if 0 in array:
        index_last_0 = array[::-1].index(0)
        if index_last_0:
            for i in range(1, len(array[-index_last_0:])+1):
                array[-i] = -1

        for item in array:
            if item != 0:
                compress_array.append(item)
        return compress_array
    return array


print(compress(given_array))
