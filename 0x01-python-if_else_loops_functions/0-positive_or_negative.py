#!/usr/bin/python3
import random
number = random.radiant(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
