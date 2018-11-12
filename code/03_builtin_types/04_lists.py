# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

animals = ["dog", "cat", "cow", "snake"]

lookup = ("dog", "horse", "cat")
found, not_found = [], []

# iterate over loopup dates
for lookup_value in lookup:
    if lookup_value in animals:
        found.append(lookup_value)
    else:
        not_found.append(lookup_value)

print("Animals found: %s" % found)
print("Animals not found: %s" % not_found)
print("First animal from the list is: %s" % animals[0])
print("Last animal from the list is: %s" % animals[-1])
print("First 2 animals: %s" % animals[:2])
print("Last 2 animals: %s" % animals[-2:])


collection = []
collection.append("milk")
collection.append("water")
collection.append("butter")
print("Collection: %s" % collection)
collection.extend(animals)
print("Collection with animals included: %s" % collection)