#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#if the number is greater than 0: is positive
#if the number is 0: is zero
#if the number is less than 0: is negative
#followed by a new line
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
