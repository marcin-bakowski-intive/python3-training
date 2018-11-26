#!/usr/bin/env python3

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']

print("Available fruits: %s" % ", ".join(fruits))
stop_fruit = input("Choose fruit, which breaks the loop? ")
skip_fruit = input("Choose fruit, which skip the loop? ")

for fruit in fruits:
    if fruit == skip_fruit:
        print("Found %s, go to next item" % skip_fruit)
        continue
    elif fruit == stop_fruit:
        print("Found %s, breaking the look" % stop_fruit)
        break
    print("Fruit: %s" % fruit)
else:
    print("Loop was not stopped with break")


fruits_names_contain_letter_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_names_contain_letter_a)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
while fruits:
    print("Current fruit: %s, there are still %d fruits left" % (fruits.pop(), len(fruits)))
