def reverse(data):
    for element in data[:: -1]:
        yield element


for char in reverse("SPAM"):
    print(char, end=" ")
print()

data = "SPAM"
for char in (elem for elem in data[::-1]):
    print(char, end=" ")
