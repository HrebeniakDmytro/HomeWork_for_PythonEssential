class ReverseIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        result = self.iterable[self.index]
        self.index -= 1
        return result

my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)
