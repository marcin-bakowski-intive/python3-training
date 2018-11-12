# for loop
for a in range(1, 3):
    print(a)

# iterate over dictionary items
animals = {
    "cat": 1,
    "dog": 2
}
for key, value in animals.items():
    print("%s=%s" % (key, value))

# iterate over animals names with index generated with enumerate builtin function
animals_list = list(animals.keys())
for idx, animal in enumerate(animals_list):
    print("Index=%s animal=%s" % (idx, animal))

# while loop
items = [1, 2, 3]
while items:
    print(items.pop())
