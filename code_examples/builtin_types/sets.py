#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

basket_1 = {'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'}

print("There are %d unique fruits." % len(basket_1))
for fruit in basket_1:
    print("This is a %s" % fruit)

basket_2 = {'orange', 'apple'}
print("Fruits in both buckets: %s" % basket_1.intersection(basket_2))
print("Fruits only in 1rst bucket: %s" % basket_1.difference(basket_2))
print("Are all fruits from 2nd basket in the 1rst bucket?: %s" % basket_2.issubset(basket_1))
print("is plum in fruits: %s" % ("plum" in basket_1))
