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
distance = 3.57 * math.sqrt(height)
print("Distance to the horizon is", distance, "km")

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
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is", average)


###
# Printing student's personal data
#
name = "Adam"
age = "23"
age = int(age)
height2 = "150"
height2 = int(height2)
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height2} cm")
print(f"In 6 years I will be {age + 6} years old.")

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

# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')

###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side = int(input('Enter cube side: '))
cube_volume = cube_side ** 3
cube_surface_area = 6 * cube_side ** 2
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_side = int(input('a='))
b_side = int(input('b='))
c_side = int(input('c='))
cube_volume2 = a_side * b_side * c_side
cube_surface_area2 = 2 * (a_side * b_side + a_side * c_side + b_side * c_side)
print(f'The volume of a box with sides {a_side}, {b_side}, {c_side} is {cube_volume2}')
print(f'The surface area of a box with sides {a_side}, {b_side}, {c_side} is {cube_surface_area2}')


### A program that calculates and prints both the amount and its VAT.
amount = float(input("Enter the amount: "))
vat = amount * 0.23
print(f"Amount: {amount:.2f}")
print(f"VAT (23%): {vat:.2f}")

### A program that calculates price with discount and reduction
price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount %: "))
discount_amount = (discount_percentage / 100) * price
discounted_price = price - discount_amount
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {discount_amount:.2f}")

###
# A program that calculates the number of characters
# of your name, surname and full name
#
name1 = 'Karol'   
surname1 = 'Matoga' 
characters_in_name = len(name1)
characters_in_surname = len(surname1)
full_name1 = name1 + ' ' + surname1
characters_in_full_name = len(full_name1)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')

###
# A program that prints your initials
#
name2 = 'George'
surname2 = 'Flinston'
print(name2[0] + surname2[0])

# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
words = university.split()
abbreviation = words[0][0] + words[1][0] + words[3][0]

print(abbreviation)

###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-11:]}')
print(f'Initials: {employee[4] + employee[9]}')

###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
formatted_phone = f'{phone[:3]}-{phone[3:6]}-{phone[6:]}'
print(f'Phone number: {formatted_phone}')


###
# A program to print numerical representations of characters.
#
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'1 {ord('1')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')

###
# A program that prints a numerical representation of each letter of your name.
#
name3 = 'Karol' # replace John with your name
print(f'The letter {name3[0]} has a code {ord(name3[0])}')
print(f'The letter {name3[1]} has a code {ord(name3[1])}')
print(f'The letter {name3[2]} has a code {ord(name3[2])}')
print(f'The letter {name3[3]} has a code {ord(name3[3])}')
print(f'The letter {name3[4]} has a code {ord(name3[4])}')



###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter second letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = abs(first_letter_code - last_letter_code) - (1 if first != last else 0)
print(f'Between {first} and {last} is {number_of_letters} letters')

###
# Character code conversion
#
print(chr(67),chr(111),chr(111),chr(108),chr(33))


# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in uppercase: ', movie.upper())

# print title in small letters
print('Title in lowercase: ', movie.lower())

# print how many times the vowel "e" appears in the title
print('Number of times "e" appears: ', movie.count('e'))

# print where in the text is the word "Lord"
print('Position of "Lord": ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('Position of "dragon": ', movie.find('dragon'))


###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
ageinput = int(input('Enter age: '))
no_tax = ageinput <= 26
print(f'Exemption from paying taxes: {no_tax}')

###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')

###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
#

numberint = int(input('Enter number: '))
even = numberint % 2 == 0
print(f'Number is even: {even}')

### A program that calculates diameter of a tree based on circumference

import math

circumference = float(input("Enter tree circumference in cm: "))
diameter = circumference / math.pi

if diameter >= 50:
    print("Tree can be cut down: True")
else:
    print("Tree can be cut down: False")


    ###
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#
car_number = input('Enter car registration number: ')
is_krakow = car_number[0:2] == "KR" or car_number[:2] == "KK"
print(f'Car is from Krakow: {is_krakow}')

### A program that checks if a vehicle speed is between 40 and 140kmh
vehicle_speed = float(input("Enter the speed: "))
if 40 <= vehicle_speed <= 140:
    print("Speed is correct.")
else:
    print("Speed is incorrect.")

    ###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)
sum = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'First dice roll: {dice_roll_1}')
print(f'Second dice roll: {dice_roll_2}')
print(f'Third dice roll: {dice_roll_3}')
print(f'Total: {sum}')

### Write a program that prints the number of dice rolled
### and the value True if the number rolled is 1 or 6
import random

dice_rolled = random.randint(1, 6)
special_number = dice_rolled == 1 or dice_rolled == 6
print(f'Dice rolled: {dice_rolled}')
print(f'Special number (1 or 6): {special_number}')


###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer = random.randint(1, 6)
# YOUR TURN
you = int(input("Guess the number: "))
win = you == computer
print(f'You won: {win}')


### A program to calculate the area and circumference of a circle.
import math  

radius = float(input('Enter the radius of the circle: '))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f'Area of the circle: {area:.2f}')
print(f'Circumference of the circle: {circumference:.2f}')


### A program that converts Celsius to Kelvin and Fahrenheit
#Read the temperature in Celsius from the keyboard
celsius = float(input("Enter temperature in degrees Celsius: "))

#Convert Celsius to Kelvin
kelvin = celsius + 273.15

#Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

#Print the results
print(f"Temperature in Kelvin: {kelvin:.2f}")
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


# A program that prints your height both in cm and in feet and inches.
cm = 170
feet = cm // 30.48
remaining_cm = cm % 30.48
inches = remaining_cm // 2.54

print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {int(inches)} inches')


# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.

swift = input('Enter SWIFT code: ')
bank_code = swift[:4]
country_code = swift[4:6]

print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')


###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distanceinput = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100km: '))
total_fuel_consumption = distanceinput * (fuel_consumption / 100)
total_cost = total_fuel_consumption * fuel_price
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Total cost of transportation: {total_cost:.2f} zł')


# A program that converts a decimal number to binary and hexadecimal

numberinput = int(input('Enter number: '))
binary_number = bin(numberinput)
hexadecimal_number = hex(numberinput)
print(f'Binary number: {binary_number}')
print(f'Hexadecimal number: {hexadecimal_number}')