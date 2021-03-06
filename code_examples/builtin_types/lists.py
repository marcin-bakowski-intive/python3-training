#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print("apple count: %s" % fruits.count('apple'))
print("tangerine count: %s" % fruits.count('tangerine'))
print("banana count: %s" % fruits.count('banana'))

print("banana index: %s" % fruits.index('banana'))
print("2nd banana index: %s" % fruits.index('banana', 4))

print("Fruit reversed: %s" % fruits.reverse())

fruits.append('grape')
print(fruits)
fruits.sort()
print("sorted fruits: %s" % fruits)

for fruit in fruits:
    print("This is a %s" % fruit)

while fruits:
    print("Let's eat %s" % fruits.pop())

print(fruits)
if not fruits:
    print("There are no fruits")

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("First fruit: %s" % fruits[0])
print("Last fruit: %s" % fruits[-1])
print("There are %d fruits" % len(fruits))
print("Let's take first 2 fruits: %s" % fruits[:2])
print("Let's take last 3 fruits: %s" % fruits[-3:])
print("Let's take every second fruit: %s" % fruits[::2])

print("is plum in fruits: %s" % ("plum" in fruits))
