#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_digit = number % 10
if number < 0:
    lst_digit = ((number * -1) % 10) * -1
if lst_digit > 5:
    print(f"Last digit of {number} is {lst_digit} and is greater than 5")
elif lst_digit == 0:
    print(f"Last digit of {number} is {lst_digit} and is 0")
elif lst_digit < 6 and lst_digit != 0:
    print(f"""Last digit of {number} is {lst_digit}
              and is less than 6 and not 0""")
