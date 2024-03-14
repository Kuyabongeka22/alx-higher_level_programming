#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a= 10
b= 5
addition= add(a, b)
print("{} + {} = {}".format(a, b, addition))

difference= sub(a, b)
print("{} - {} = {}".format(a, b, difference))

product= mul(a, b)
print("{} * {} = {}".format(a, b, product))

quotient= div(a, b)
print("{} / {} = {}".format(a, b, quotient))
