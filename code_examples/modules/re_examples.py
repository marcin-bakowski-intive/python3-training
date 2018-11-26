import re


def print_match_status(re_compiled_pattern, string):
    match = re_compiled_pattern.match(string)
    print("Does '%s' match pattern %s? %s" % (string, re_compiled_pattern, bool(match)))
    return match


print(re.findall("a.c", " abc aac aa abb a c "))

pattern = re.compile("^c.*t$")
print_match_status(pattern, "cat")
print_match_status(pattern, "caaat")
print_match_status(pattern, "at")

pattern = re.compile("^[a-z]+$")
print_match_status(pattern, "123")
print_match_status(pattern, "cat")
print_match_status(pattern, "Cat")

pattern = re.compile("^[^a-z]+$")
print_match_status(pattern, "123")
print_match_status(pattern, "cat")
print_match_status(pattern, "Cat")

pattern = re.compile("^\w+$")
print_match_status(pattern, "123")
print_match_status(pattern, "cat")
print_match_status(pattern, "cat!")

pattern = re.compile("^\d+$")
print_match_status(pattern, "123")
print_match_status(pattern, "cat")

pattern = re.compile("^(\w+) (\w+)$")
print_match_status(pattern, "123")
match = print_match_status(pattern, "funny cat")

# print whole match
print(match.group(0))
# print matching 1rst group
print(match.group(1))
# print matching 2nd group
print(match.group(2))


pattern = re.compile("^(\w{1,3}) (\w{3})$")
print_match_status(pattern, "funny cat")
match = print_match_status(pattern, "a cat")
print(match.groups())

match = print_match_status(pattern, "bad dog")
print(match.groups())
