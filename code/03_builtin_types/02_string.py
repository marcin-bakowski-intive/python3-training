# Strings
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
animal = "beagle dog"
print("This is a %s" % animal.upper())
print("Partial string: %s" % animal[:6])
print("Partial string from the end: %s" % animal[-3:])
print("Let's replace dog: %s" % animal.replace("beagle", "husky"))

animals = "%s and husky dog" % animal
print(animals)

