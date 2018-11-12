# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

animals = ("dog", "cat")

lookup = ("dog", "horse", "cat")

for lookup_value in lookup:
    if lookup_value in animals:
        print("'%s' found in animals tuple" % lookup_value)
    else:
        print("'%s' not found in animals tuple" % lookup_value)
