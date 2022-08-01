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


# 10. Write a Python program to print the following 'here document'.
# Sample string: a string that you "don't" have to escape This is a ....... multi-line heredoc string --------> example
# Sample Output:
#
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

# 11. Write a Python program to create a new string where "if" is added to the front of a given string.
# If the string already begins with "if", return the string unchanged.
# Sample Output:
# if else
# if else

given_string = 'if else'


def add_if(string):
    if string.startswith('if'):
        return string
    return 'if ' + string


print(add_if(given_string))


# 12. Write a Python program to create a new string from a given string using the first three characters or
# whatever is there if the string is less than length 3. Return n copies of the string.
# Sample Output:
# abc
# abcabc
# abc
# abcabc
# abc
# abab

given_string = 'abc'
N = 2


def n_copies(string, n):
    return string * n if len(string) <= 3 else string[:3] * n


print(n_copies(given_string, N))


# 13. Write a Python program which accepts the radius of the sphere as input and compute the volume.
# Sample Output:
# Input the radius of the circle: The volume of the sphere is: 392.699081625.

import math


def volume_sphere(radius):
    return 4/3 * math.pi * radius**3


print(f"The volume of the sphere is: {volume_sphere(4)} ")


# 14. Write a Python program to create a new string from a given string where the first and
# last characters have been exchanged.
# Sample Output:
# nythoP
# aavJ

given_string = 'Java'


def exchange_letter(string):
    return string[-1] + string[1:-1] + string[0]


print(exchange_letter(given_string))


# 15. Write a Python program to check two integers and return true if one of them is 20 otherwise return their sum.

def check_int(num1, num2):
    return True if num1 == 20 or num2 == 20 else num1+num2


print(check_int(20, 22))


# 16. Write a Python program to find the greatest of three numbers.
# Sample Output:
# y = 5 is greatest.

def greatest(num1, num2, num3):
    return max(num1, num2, num3)


print(f"{greatest(1, 5, 3)} is greatest")


# 17. Write a Python program to check if a number is within 10 of 100 or 200. (E.g. 90, 110, 190, 210)

def if10(number):
    return abs(100 - number) == 10 or abs(200 - number) == 10


print(if10(120))


# 18. Write a Python program to compute the sum of the two integers,
# if the two values are equal return double their sum otherwise return their sum.
# Sample Output:
# 20
# 9

def sum_two(val1, val2):
    return 2 * (val1 + val2) if val1 == val2 else val1 + val2


print(sum_two(5, 1))


# 19. Write a Python program to print “Python Basic Exercises" 9 times.

string = "Python Basic Exercises"
for i in range(9):
    print(string)


# 20. Write a Python program to create a new string from a given string with the last character
# added at the front and back of the given string. The length of the given string must be 1 or more.
# Sample Output:
# cabcc
# dabcdd
# ajavaa

given_string = 'java'


def add_front_back(string):
    if len(string) >= 1:
        return string[-1] + string + string[-1]
    return False


print(add_front_back(given_string))


# 21. Write a Python program to print 34 upto 41.
# Sample Output:
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42

for i in range(34, 43):
    print(i)


# 22. Write a Python program to print even numbers from 1 to 10.
# Sample Output:
# Even numbers between 2 to 10:
# 2
# 4
# 6
# 8
# 10

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# 23. Write a Python program to print odd numbers from 10 to 1.
# Sample Output:
# Odd numbers between 9 to 1:
# 9
# 7
# 5
# 3
# 1

for i in reversed(range(1, 10)):
    if i % 2 == 1:
        print(i)


# 24. Write a Python program to print the elements of a given array. Sample array : ["Ruby", 2.3, Time.now]

from datetime import datetime as Time

for item in ["Ruby", 2.3, Time.now]:
    print(item)


# 25. Write a Python program to check two non-negative integer values and return true
# if they have the same last digit.

def non_negative(num1, num2):
    return num1 % 10 == num2 % 10


print(non_negative(101, 2341))


# 26. Write a Python program to retrieve the total marks where subject name and marks of a student stored in a hash.
# Sample subject and marks: Literature -74, Science – 89, Math-91
# Sample Output:
# Total Marks: 254

student_hash = {'Literature': 74, "Science": 89, "Math": 91}


def total_marks(student):
    total = 0
    for value in student.values():
        total += value
    return total


print(total_marks(student_hash))


# 27. Write a Python program to print a specified character twenty times.
# Sample Output:
# ********************
# ####################
# @@@@@@@@@@@@@@@@@@@@

print("*"*20)


# 28. Write a Python program to test whether a year is leap year or not.
# Sample Output:
# 2012 is leap year
# 1500 is not leap year
# 1600 is leap year
# 2020 is leap year

given_year = 2012


def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


print(leap_year(given_year))


# 29. Write a Python program to check whether a string 'Java' appears at index 1 in a given sting,
# if 'Java' appears return the string without 'Java' otherwise return the string unchanged.
# Sample Output:
# Script
# Oldjava

given_string = 'Java Script'


def apears_java(string):
    return string[4:] if string[:4] == 'Java' else string


print(apears_java(given_string))


# 30. Write a Python program to create a string using the first two characters
# (if present) of a given string if the first character is 'p' and second one is 's' otherwise return a blank string.
# Sample Output:
# ps

giving_string = 'psjfj'


def first_two(string):
    return 'ps' if string[:2] == 'ps' else ''


print(first_two(giving_string))


# 31. Write a Python program to check two integers and return whichever value is nearest to the value 10,
# or return 0 if two integers are equal.
# Sample Output:
# 7
# 9
# 0

def nearest10(num1, num2):
    if abs(10-num1) < abs(10-num2):
        return num1
    elif abs(10-num1) > abs(10-num2):
        return num2
    else:
        return 0


print(nearest10(11, 8))


# 32. Write a Python program to check two integer values and return true
# if they are both in the range 10..20 inclusive, or they are both in the range 20..30 inclusive.
# Sample Output:
# true
# false
# true
# false

def both_in_range(num1, num2):
    range_10_20 = range(10, 21)
    range_20_30 = range(20, 31)
    if num1 in range_10_20 and num2 in range_10_20:
        return True
    if num1 in range_20_30 and num2 in range_20_30:
        return True
    return False


print(both_in_range(10, 20))


# 33. Write a Python program to check two positive integer values and return the larger value
# that is in the range 20..30 inclusive, or return 0 if no number is in that range.
# Sample Output:
# 0
# 29
# 30
# 0

def return_larger(num1, num2):
    range_20_30 = range(20, 31)
    if num1 in range_20_30 and num2 in range_20_30:
        return num1 if num1 > num2 else num2
    return 0


print(return_larger(34, 25))


# 34. Write a Python program to count the number of 5's in a given array.
# Sample Output:
# 0
# 1
# 2

given_array = [33, 16, 5, 1, 5, 6, 12]


def count5(array):
    count = 0
    for item in array:
        if item == 5:
            count += 1
    return count


print(count5(given_array))


# 35. Write a Python program to check two non-negative integer values and return true if
# they have the same last digit.

def non_negative(num1, num2):
    return num1 % 10 == num2 % 10


print(non_negative(101, 2341))


# 36. Write a Python program to check if the sequence of numbers 10, 20, 30 appears anywhere
# in a given array of integers

given_array = [1, 2, 10, 20, 30, 2, 4]


def sequence_102030(array):
    i = 0
    check = None
    while i < len(array) - 2:
        if array[i:i+3] == [10, 20, 30]:
            check = True
            break
        else:
            check = False
        i += 1
    return check


print(sequence_102030(given_array))


# 37. Write a Python program to check two given integers and return 11 if either one is 11.
# Return their sum or difference if sum or difference is 11

def check11(num1, num2):
    if num1 == 11 or num2 == 11 or num1 + num2 == 11 or num1 - num2 == 11:
        return 11
    return False


print(check11(111, 100))


# 38. Write a Python program to check three given integers and return true if one of them is 20
# or more less than one of the others

def diff20(num1, num2, num3):
    if abs(num1-num2) == 20 or abs(num1-num3) == 20 or abs(num2-num3) == 20:
        return True
    return False


print(diff20(17, 27, 37))


# 39. Write a Python program to check two given integers and return the larger value.
# However, if the two values have the same remainder when divided by 5 then return the smaller value
# and if the two values are the same, return 0.
# Sample Output:
# 12
# 110
# 0

def remainder5(num1, num2):
    if num1 == num2:
        return 0
    elif num1 % 5 == num2 % 5:
        return min(num1, num2)
    return max(num1, num2)


print(remainder5(12, 12))


# 40. Write a Python program to check two given integers, each in the range 10..99,
# return true if there is a digit that appears in both numbers.

def appears_in_both(num1, num2):
    d1_1 = num1 // 10
    d2_1 = num2 // 10
    d1 = num1 % 10
    d2 = num2 % 10
    return d1 == d2 or d2_1 == d1_1 or d1 == d2_1 or d2 == d1_1
# or
    # str_1 = str(num1)
    # str_2 = str(num2)
    # check = False
    # for digit in range(10):
    #     str_digit = str(digit)
    #     if str_digit in str_1 and str_digit in str_2:
    #         check = True
    #         break
    # return check


print(appears_in_both(21, 41))


# 41. Write a Python program to check three given integers x, y, z and return true
# if one of y or z is close (differing from a by at most 1), while the other is far,
# differing from both other values by 3 or more.


def check_xyz(x, y, z):
    if abs(y-z) >= 3:
        return abs(x - y) == 1 and abs(x-z) >= 3 or abs(x-z) == 1 and abs(x-y) >= 3
    return False


print(check_xyz(1, 7, 2))


# 42. На зустріч один одному відповідно з міста А та міста Б рухається заєць та черепаха.
# Ввести з клавіатури відстань між містами, швидкість зайця та швидкість черепахи.
# Обчислити на якій відстані від міста Б вони зустрінуться.

def meet_dist():
    dist_AB = int(input('Enter distance between A and B: '))
    speed_r = int(input('Enter the rabbit speed: '))
    speed_t = int(input('Enter the turtle speed: '))

    return dist_AB / (1 + speed_r/speed_t)


print(f"They will meet at a distance of {meet_dist()} from B city")


# 43. З міста А в місто Б їде велосипедист. З його плеча злітає муха. Вона летить до міста Б,
# долітає до нього та повертається назад. Знову долітає до велосипедиста, розвертається і летить до міста Б...
# і так до тих пір, поки велосипедист не доїде до пункту Б. Відомо відстань між містами, швидкість велосипедиста
# та швидкість мухи. Написати програму, що визначає скільки кілометрів налітає муха.

def amount_of_km(dist, speed_b, speed_f):
    t_b = dist/speed_b
    return t_b * speed_f


print(amount_of_km(10, 2, 3))


# 44.Написати програму, яка визначає дату наступного дня, на основі сьогоднішньої дати.

import datetime
print(datetime.datetime.now().day+1)


# 45. Написати программу, яка задає категорію та стаж працівника, а також ставку відповідно докатегорії
# (1-ша категорія—3000, 2-га – 2000, 3-тя -- 1000). Обчислити заробітну плату, враховуючи надбавку за
# стаж роботи(до 2 років—0%, від 2 до 5 – 10%, від 5 до 10 – 20%, більше 10—30% ) і зняття податку – 15%.

def rate(cat):
    if cat == 1:
        return 3000
    elif cat == 2:
        return 2000
    elif cat == 3:
        return 1000


def extra_tax(exp):
    TAX = 0.85
    coef = 1
    if 2 <= exp < 5:
        coef = 1.1
    elif 5 <= exp < 10:
        coef = 1.2
    elif exp >= 10:
        coef = 1.3
    return coef*TAX


category = 1
experience = 7
if category in range(1, 4):
    print(rate(category)*extra_tax(experience))
else:
    print('The category could be only 1, 2 or 3')


# 46. Написати програму, яка із введеного користувачем цілого чотирьохзначного числа (наприклад 5141):
# знаходить суму цифр цього числа (5141 це 5+1+4+1 = 11).
# перевіряє чи є однакові цифри (двічі зустрічається цифра 1)
# перевіряє чи сума двох перших цифр чотирьохзначного числа рівна двом наступним
# (5141 → 5+1 = 6 і 4+1 = 5 → суми першої та другої пар цифр даного числа різні)

def some_operations(num):
    digit1 = num // 1000
    digit2 = num // 100 % 10
    digit3 = num // 10 % 10
    digit4 = num % 10

    summ = digit1 + digit2 + digit3 + digit4

    unrepeat = []
    if len([unrepeat.append(item) for item in str(num) if item not in unrepeat]) != 4:
        repeat = True
    else:
        repeat = False

    equal = True if digit1+digit2 == digit3+digit4 else False

    return summ, repeat, equal


print(some_operations(7227))


# 47. Написати програму, яка обчислює, скільки повинен заплатити водій за паркування автомобіля на стоянці
# протягом певного часу. Користувач вводить наступні дані: час заїзду на стоянку (у годинах і хвилинах),
# час від’їзду, вартість однієї години паркування. Водій платить за кожну повну годину. Також, здійснюється
# плата за перевищення користування стоянкою більше ніж на 10 хв., наприклад: якщо хтось використав стоянку
# протягом 2 год. і 15 хв., то повинен заплатити за 3 год. В кінцевому результаті на екран необхідно вивести
# повідомлення про час заїзду та виїзду авто, ціну за годину паркування і повну вартість.

def parking():
    start = input('Start time (hh:mm): ').split(':')
    stop = input('Stop time (hh:mm): ').split(':')
    price = int(input('Price for 1 hour: '))

    parking_time = int(stop[0]) - int(start[0])
    if abs(int(stop[1]) - int(start[1])) > 10:
        parking_time += 1

    return f"\n Enter time: {':'.join(start)}\n Exit time: {':'.join(stop)}\n Price for one hour: {price}\n " \
           f"Total price: {parking_time*price}"


print(parking())
