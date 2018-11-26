from contextlib import contextmanager


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


@contextmanager
def open_file(file_name, method):
    f = open(file_name, method)
    yield f
    f.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hello!!!')


with open_file('demo2.txt', 'w') as opened_file:
    opened_file.write('Hello!!!')
