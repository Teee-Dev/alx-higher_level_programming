#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

# Perform addition and print the result
result_add = add(a, b)
print("{} + {} = {}".format(a, b, result_add))

# Perform subtraction and print the result
result_sub = sub(a, b)
print("{} - {} = {}".format(a, b, result_sub))

# Perform multiplication and print the result
result_mul = mul(a, b)
print("{} * {} = {}".format(a, b, result_mul))

# Perform division and print the result
result_div = div(a, b)
print("{} / {} = {}".format(a, b, result_div))
