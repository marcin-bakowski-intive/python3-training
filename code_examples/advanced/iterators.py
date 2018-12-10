class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.index = len(self.data)
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


for char in Reverse("SPAM"):
    print(char, end=" ")
