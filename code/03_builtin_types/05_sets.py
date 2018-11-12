# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

animals = ["dog", "cat", "snake", "dog", "snake"]
unique_animals = set(animals)
animals_collection = {"cat", "dog", "cow", "horse"}

print("Number of all animals: %s, %s" % (len(animals), animals))
print("Number of unique animals: %s, %s" % (len(unique_animals), unique_animals))
print("There are %s present in both collections" % animals_collection.intersection(unique_animals))
