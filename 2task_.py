# 1. Write Python program to get the version(not inside iterpretator).
import sys
print(sys.version)


# 2. Write Python program to display the current date and time.
#
# Sample Output:
# Current Date and Time: 27/12/2017 06:04
import datetime
now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y %H:%M"))


# 3. Write a Python program to create a new string which is n copies of a given string
# where n is a non-negative integer.
#
# Sample Output:
# a
# aa
# aaa
# aaaa
# aaaaa

given_string = 'a'


def n_copies(string, number):
    return string * number


print(n_copies(given_string, 4))


# 4. Write a Python program which accepts the radius of a circle from the user and compute the parameter and area.
# Sample Output:
# Input the radius of the circle: The perimeter is 31.41592653.
# The area is 78.539816325.

import math


def area_parameter(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area


print(f"The perimeter is {area_parameter(8)[0]}\nThe area is {area_parameter(8)[1]} ")


# 5. Write a Python program to check if a string starts with "if".
# Sample Output:
# true
# false

given_string = 'if I do something'


def start_with(string):
    return string.startswith('if')


print(start_with(given_string))


# 6. Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.
# Sample Output:
# Input your first name:
# Input your last name:
# Hello Lanoie Gary

first_name = input('Input your first name: ')
last_name = input('Input your last name: ')

print(f'Hello {last_name} {first_name}')


# 7. Write a Python program to accept a filename from the user to print the extension of that. (With Regexp)
# Sample Output:
# Filename: test.rb
# Base name: test
# Extension: .rb
# Pathname: /user/system

import re

file_name = input('Filename: ')


def print_extension(filename):
    # template = r'\.[a-z]{,}'
    match = re.split(r'\.', filename)
    print(f"Filename: {filename}")
    print(f"Base name: {match[0]}")
    print(f"Extension: .{match[1]}")
    return match


print_extension(file_name)


# 8. Write a Python program to check three numbers and return true if one or more of them are small.
# A number is called "small" if it is in the range 1..10 inclusive.
# Sample Output:
# true
# true
# false

def check_three(num1, num2, num3):
    small = range(1, 11)
    return num1 in small or num2 in small or num3 in small


print(check_three(3, 23, 33))


# 9. Write a Python program to check three numbers and return true if one or the other is small, but not both.
# A number is called "small" if it is in the range 1..10 inclusive.
# Sample Output:
# true
# true
# false

def check_three(num1, num2, num3):
    small = range(1, 11)
    check_1 = num1 in small
    check_2 = num2 in small
    check_3 = num3 in small
    if check_1 and not check_2 and not check_3:
        return True
    elif check_2 and not check_1 and not check_3:
        return True
    elif check_3 and not check_1 and not check_2:
        return True
    else:
        return False


print(check_three(37, 88, 3))


