class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        
        result = (self.index, self.iterable[self.index])
        self.index += 1
        return result

my_list = ['x', 'y', 'z', 'w']
for index, value in MyIterable(my_list):
    print(index, value)
