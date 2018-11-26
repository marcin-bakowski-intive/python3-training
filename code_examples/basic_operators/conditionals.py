#!/usr/bin/env python3

# if statement
fruit = "apple"
if fruit == "orange":
    print("This is an orange")
elif fruit == "apple":
    print("This is an apple")
else:
    print("Unknown fruit")

print("Is this fruit an apple? %s" % (fruit == "apple"))
print("Is this fruit an apple? %s" % ("yes" if fruit == "apple" else "no"))

x = int(input("Please enter an integer: "))
if x < 0:
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
