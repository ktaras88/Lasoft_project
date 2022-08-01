# 37. In a two-dimensional array of order M and N, swap the specified columns.

given_array = [[1, 2, 3], [1, 2, 3]]


def swap(array, n, m):
    for item in array:
        item[n], item[m] = item[m], item[n]
        print(item)


swap(given_array, 1, 2)
