# if statement

items = [1, 2, 3]
if 1 in items:
    print("Found 1 in %s" % items)
else:
    print("1 not found")

# single-line if statement
found_message = "found" if 1 in items else "not found"
print(found_message)

# boolean expression
print(1 in items)
