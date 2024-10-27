###
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 23
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

    ###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
x = y
y = x

print("After swapping: x=", x, "y=", y)

###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh * 1000
print(speed_kmh, "km/h = ", speed_ms, "m/s")

###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)

###
# A program that calculates the distance to the horizon from a height given in meters from the keyboard
import math
height = input('Enter the height in meters: ')
height = int(height)
distance = height * 1000
distance = 3.57 * math.sqrt(height)

###
# A program that calculates the distance to the horizon from a height given in meters from the keyboard
import math
height = input('Enter the height in meters: ')
height = int(height)
distance = 3.57 * math.sqrt(height)
distance2 = distance * 1000
print("Distance to the horizon is", distance2, "km")

###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)

###
# Printing student's personal data
#
name = "Adam"
age = "23"
age = int(age)
height = "150"
height = int(height)
agesix = age + 6
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm")
print(f"In 6 years I will be {agesix} years old.")

###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person}')

a = 3
b = 5
print(f'{a}+{b}= {a +b}')
print(f'{a}-{b}= {a - b}')
print(f'{a}*{b}= {a * b}')
print(f'{a}/{b}= {a/b}')
