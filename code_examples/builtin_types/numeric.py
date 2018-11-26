#!/usr/bin/env python3
a = 10
b = -5.5
c = "123.11"

print("Sum: %.2f " % sum([a, b]))
print("Integer sum: %d " % sum([a, b]))
print("Divide: %.3f" % (a / 3.0))
print("Decimal {value}, binary {value:b}".format(value=a))

print("Data type conversion: original value=%s (%s)" % (c, type(c)))
c_float = float(c)
print("After conversion to float: value=%f (%s)" % (c_float, type(c_float)))

print("Rounded: %s" % round(c_float, 1))
print("Absolute value: %s" % abs(b))

# arthritic operators
number = 2 + 3 * 3 / 3.0
print(number)

# modulo operator
remainder = 8 % 3
print(remainder)

# Using two multiplication symbols makes a power relationship.
squared = 2 ** 2
cubed = 2 ** 3
print(squared, cubed)
