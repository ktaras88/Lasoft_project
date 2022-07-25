# 27. Write a Python program to convert an array into a hash.
# Sample Output:
# Original array:
# [(10, 5), (20, 3), (30, 4), (10,2)]
# Hash:
# {10:(5,2), 20:(3), 30:(4)}

original = [(10, 5), (20, 3), (30, 4), (10, 2)]


def convert_into_hash(array):
    a_hash = {}
    for element in array:
        if element[0] not in a_hash:
            a_hash[element[0]] = element[1]
        else:
            a_hash[element[0]] = (a_hash[element[0]], element[1])
    print(a_hash)


convert_into_hash(original)
