def get_sum(x, y):
    return x + y


print("get_sum(): %s" % get_sum(1, 1))


# function with *args
def get_sum_unlimited_args(*args):
    return sum(args)


print("get_sum_unlimited_args: %s" % get_sum_unlimited_args(1, 2, 3, 4, 5))


# function with default parameters
def increment(value, step=1):
    return value + step


print("Increment fn: %s" % increment(1))
print("Increment fn: %s" % increment(1, 2))
print("Increment fn: %s" % increment(1, step=3))


# function with args and kwargs
def sum_elements(*args, **kwargs):
    odd_only = kwargs.get("odd_only", None)
    items = [v for v in args if v % 2 == 0] if odd_only else args
    return sum(v for v in items)


print("Sum elements: %s" % sum_elements(1, 2, 3))
print("Sum elements: %s" % sum_elements(1, 2, 3, odd_only=True))

# anonymous lambda function
to_lower = lambda x: x.lower()
for val in ["b", "A", "C"]:
    print("to_lower(%s) is %s" % (val, to_lower(val)))

# Check Python3 builtin functions
# https://docs.python.org/3/library/functions.html
