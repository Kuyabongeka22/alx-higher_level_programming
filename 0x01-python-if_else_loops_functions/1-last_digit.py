#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
condition_3 = "is less than 6 and not 0"
if number > 5:
    print(f"Last digit of {number} is {number % 10} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
elif number < 6 |number != 0:
    print(f"Last digit of {number} is {number % 10} and {condition_3}")
else:
    print(f"Last digit of {number} is {number % 10}")
