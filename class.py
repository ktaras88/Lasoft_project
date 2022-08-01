# 1. Write a Python class named Circle constructed by a radius and two methods which will compute
# the area and the perimeter of a circle.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius


# 2. Write a Python class named Rectangle constructed by a length and width
# and a method which will compute the area of a rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


# 3. Write a Python class to reverse a string word by word.

class ReverseStr:
    def __init__(self, string):
        self.string = string

    def reverse_words(self):
        return ' '.join(self.string.split()[::-1])


# 4. Write a Python class to implement pow(x, n).

class Exponentiation:
    def __init__(self, number, power):
        self.number = number
        self.power = power

    def expo(self):
        if self.power == 0:
            return 1
        num = self.number if self.power > 0 else 1 / self.number
        temp = 1
        for i in range(abs(self.power)):
            temp *= num
        return temp


# 5. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets
# must be close in the correct order,for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class Validation:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        valid = {'(': ')', '{': '}', '[': ']'}
        check = None
        for bracket in self.string:
            if bracket in valid:
                if valid[bracket] in self.string:
                    check = True
                else:
                    check = False
                    break
        return check


str1 = Validation('({[)]')
print(str1.is_valid())


# 6. Define a class called Lunch.Its __init__() method should have two arguments:self and menu.Where menu is a string.
# Add a method called menu_price.It will involve a if statement:
# if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40",
# else print "Error in menu".
# To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().

class Lunch:
    def __init__(self, menu: str):
        self.menu = menu

    def menu_price(self):
        if self.menu == 'menu 1':
            pr = f"Your choice: {self.menu} Price 12.00"
        elif self.menu == 'menu 2':
            pr = f"Your choice: {self.menu} Price 13.40"
        else:
            pr = "Error in menu"
        return pr


Paul = Lunch('menu 1')
print(Paul.menu_price())


# 7. Define a Point3D class that inherits from object Inside the Point3D class, define an __init__() function
# that accepts self, x, y, and z, and assigns these numbers to the member variables self.x,self.y,self.z.
# Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent
# this object in the following format: (x, y, z). Outside the class definition, create a variable named my_point
# containing a new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point)


# 8. Define a class called Songs, it will show the lyrics of a song. Its __init__() method should have two
# arguments:self and lyrics.lyricsis a list. Inside your class create a method called sing_me_a_songthat
# prints each element of lyricson his own line. Define a variable:
# happy_bday = Song(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"])
#
# Call the sing_me_songmehod on this variable.


class Song:
    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
happy_bday.sing_me_a_song()
