#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif number < 0:
    print(f"Last digit of {number} is {(abs(number) % 10) * -1} and is less than 6 and not 0")
elif last < 6:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is greater than 5")
