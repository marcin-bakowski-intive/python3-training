# fill list in for loop
examples = []
for i in range(10):
    examples.append(i)
print(examples)

# fill list in-line
examples2 = [i for i in range(10)]
print(examples2)

# conditional list comprehension
examples3 = [i for i in range(10) if i < 3]
print(examples3)
