# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

animals = {"cat": 2,
           "dog": 1,
           "snake": 0,
           "house": 1
           }


def is_animal_present(animal):
    if animal in animals:
        print("Found %s %ss" % (animals[animal], animal))
        return True
    else:
        print("%s not found" % animal)
        return False


def animals_summary():
    print("There are %s available." % ", ".join(animals.keys()))
    print("There are %s animals found." % sum(animals.values()))

animals_summary()
is_animal_present("cat")
is_animal_present("chicken")

print("Let's increase animals population")
for key in animals.keys():
    animals[key] += 1

print(animals)
animals_summary()

print("We decided to get rid of snakes")
animals.pop("snake")
animals_summary()
