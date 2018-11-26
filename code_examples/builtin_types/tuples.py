#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

animals = ("dog", "cat")

lookup = ("dog", "horse", "cat")

for lookup_value in lookup:
    if lookup_value in animals:
        print("'%s' found in animals tuple" % lookup_value)
    else:
        print("'%s' not found in animals tuple" % lookup_value)


fruits = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')

print("apple count: %s" % fruits.count('apple'))
print("tangerine count: %s" % fruits.count('tangerine'))
print("banana count: %s" % fruits.count('banana'))

print("banana index: %s" % fruits.index('banana'))
print("2nd banana index: %s" % fruits.index('banana', 4))


for fruit in fruits:
    print("This is a %s" % fruit)

print("There are %d fruits" % len(fruits))

fruits = ('orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana')
print("First fruit: %s" % fruits[0])
print("Last fruit: %s" % fruits[-1])
print("There are %d fruits" % len(fruits))
print("Let's take first 2 fruits: %s" % (fruits[:2],))
print("Let's take last 3 fruits: %s" % (fruits[-3:],))
print("Let's take every second fruit: %s" % (fruits[::2],))

print("is plum in fruits: %s" % ("plum" in fruits))
