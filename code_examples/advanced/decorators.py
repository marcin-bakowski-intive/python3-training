from functools import wraps


def shout(fn):
    """ Function appends '!!!' to the original result"""
    def decorated(name):
        ret = fn(name)
        print("Function '%s' returned '%s'" % (fn.__name__, ret))
        return "%s!!!" % ret
    return decorated


@shout
def hello(name):
    return "Hello %s" % name.capitalize()


def shout2(fn):
    """ Function appends '!!!' to the original result"""
    @wraps(fn)
    def decorated(name):
        ret = fn(name)
        print("Function '%s' returned '%s'" % (fn.__name__, ret))
        return "%s!!!" % ret
    return decorated


@shout2
def hello2(name):
    return "Hello %s" % name.capitalize()


print("Call results: '%s'" % hello("marcin"))
print(hello)

print("Call results: '%s'" % hello2("marcin"))
print(hello2)
