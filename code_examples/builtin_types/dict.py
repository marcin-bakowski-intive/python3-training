#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

basket_1 = {'orange': 1,
            'apple': 2,
            'pear': 1,
            'banana': 3,
            'kiwi': 2}

print(basket_1)
for fruit, quantity in basket_1.items():
    print("There are %s %s" % (quantity, fruit))

basket_2 = {'orange': 0, 'apple': 10}
basket_1.update(basket_2)
for fruit in basket_1:
    print("There are %s %s" % (basket_1[fruit], fruit))

print(basket_1)
print("There are %s fruits in basket 1" % sum(basket_1.values()))

print("is plum in fruits: %s" % ("plum" in basket_1))
print("Get plum: %s" % basket_1.get('plum', "sorry, no plum found"))
print("Get plum: %s" % basket_1['plum'])
