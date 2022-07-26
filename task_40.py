# 40. Given the single-mass array. Cyclically shift the array on the K elements, on the right or left side

given_array = [1, 2, 3, 4, 5]
K = 1
sides = 'right'


def cyclically_shift(array, side, k):
    print(f'Given single-mass array:\n{array}')
    shifted = []
    len_shifted = 0
    for i in range(len(array)):
        if side == 'left':
            if i+k < len(array):
                shifted.append(array[i+k])
                len_shifted += 1
            else:
                shifted.append(array[i-len_shifted])
        elif side == 'right':
            if i+k < len(array):
                shifted.append(array[-k+i])
            else:
                shifted.append(array[i-k])
    print(f'Cyclically shifted:\n{shifted}')


cyclically_shift(given_array, sides, K)
