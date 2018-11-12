
# ignore exception
try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
    pass


# re-raise exception
try:
    1 / 0
except ZeroDivisionError as e:
    print("Re-raise exception %s" % e)
    raise e

