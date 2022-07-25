# 9. Write a Python program to split a delimited string into an array.
# Sample Output:
# Original delimited string:
# Red, Green, Blue, White1, 3, 4, 5, 7String to array:
# ["Red", " Green", " Blue", " White"]
# [1, 3, 4, 5, 7]
import re

delimited_string = 'Red, Green, Blue, White1, 3, 4, 5, 7'


def string_to_array(string):
    template_words = '[A-Z][a-z]{2,}'
    template_digit = r'\d'

    words = re.findall(template_words, string)
    digits = re.findall(template_digit, string)

    print(words)
    print(list(map(int, digits)))

# or

    # separable_index = string.find('1')
    # words = string[:separable_index].split(',')
    # digits = string[separable_index:].split(',')
    # print(words)
    # print([int(x) for x in digits])


string_to_array(delimited_string)
