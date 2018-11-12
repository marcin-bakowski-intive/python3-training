# arthritic operators
number = 2 + 3 * 3 / 3.0
print(number)

# modulo operator
remainder = 8 % 3
print(remainder)

# Using two multiplication symbols makes a power relationship.
squared = 2 ** 2
cubed = 2 ** 3
print(squared, cubed)


# string concatenation
helloworld = "hello" + "_" + "world"
print(helloworld)

# string multiplication
hellos = "HELLO" * 10
print(hellos)

# list concatenation
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# in operator
print("Is %d in %s: %s" % (1, even_numbers, 1 in even_numbers))
print("Is %d in %s: %s" % (2, even_numbers, 2 in even_numbers))
print("Is '%s' in '%s': %s" % ("hello", helloworld, "hello" in helloworld))


# is operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
