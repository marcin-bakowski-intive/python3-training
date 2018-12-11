#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

test_string = "test string"
test_string2 = 'test string'
test_string_multi_line = """
test multi lines
"""
test_string3 = str(1.0)
print(test_string[0])       # prints first character: t
print(test_string[-1])      # prints last character: g
print(test_string[:4])	    # print slice of string (first 4 characters) -> test
print(test_string[-6:])	    # print slice of string (last 6 characters) -> string
print(test_string[-11:])    # print "test string" using negative indexing
print(test_string[::-1])    # revingersed str

animal = "beagle dog"
print("This is a %s" % animal.upper())
print("Partial string: %s" % animal[:6])
print("Partial string from the end: %s" % animal[-3:])
print("Let's replace dog: %s" % animal.replace("beagle", "husky"))

animals = "%s and husky dog" % animal
print(animals)


# Format string using format() method
# using positional arguments
print("This is test no. {}".format(1))
# using kwargs 
print("This is test no. {test_number}".format(test_number=2))
# print float with 2 digits precision
test_number = 1.0
print("This is test no: {:.2f}".format(test_number))

# Format sting using printf-style
test_number = 1.0
# print float as string
print("This is test no: %s" % test_number)
# print float with 2 digits precision
print("This is test no: %.2f" % test_number)
