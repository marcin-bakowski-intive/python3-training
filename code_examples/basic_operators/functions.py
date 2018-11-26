def hello_world():
    print("Hello World !!")


def get_sum(x, y):
    """
    returns x + y sum

    :param x:
    :param y:
    :return:
    """
    return x + y


# function with *args
def get_sum_unlimited_args(*args):
    return sum(args)


# function with default parameters
def increment(value, step=1):
    """
    Increments given value

    :param value: value to increment (numeric type)
    :param step: increment step (numeric type)
    :return:
    """
    return value + step


def noop():
    """
    No operation function
    :return: None
    """
    pass


# function with args and kwargs
def sum_elements(*args, **kwargs):
    odd_only = kwargs.get("odd_only", None)
    items = [v for v in args if v % 2 == 0] if odd_only else args
    return sum(v for v in items)


hello_world()
print("get_sum(): %s" % get_sum(1, 1))
print("get_sum_unlimited_args: %s" % get_sum_unlimited_args(1, 2, 3, 4, 5))
print("Increment fn: %s" % increment(1))
print("Increment fn: %s" % increment(1, 2))
print("Increment fn: %s" % increment(1, step=3))
print("Sum elements: %s" % sum_elements(1, 2, 3))
print("Sum elements: %s" % sum_elements(1, 2, 3, odd_only=True))


# anonymous lambda function
to_lower = lambda x: x.lower()
for val in ["b", "A", "C"]:
    print("to_lower(%s) is %s" % (val, to_lower(val)))

# Check Python3 builtin functions
# https://docs.python.org/3/library/functions.html
