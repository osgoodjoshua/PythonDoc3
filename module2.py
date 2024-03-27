# this module is used for hw exercise #2

from math import pi


# 1
def house_sqft():
    length = input('What is the length of your house? ')
    width = input('What is the width of your house? ')
    area = int(length) * int(width)
    print(f'The area of your house is {area} square feet.')


    
# 2
def circumference():
    radius = input('What is the radius of the circle? ')
    total = 2 * pi * int(radius)
    print(f'The total circumference is: {total}')
    
    