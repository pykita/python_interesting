class SimpleIterator:
    def __iter__(self):
        return self
 
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
 
    def __next__(self):
        if self.counter < self.limit:
            self.counter = self.counter + 1
            yield self.counter 
        else:
            raise StopIteration
 
simple_iter = iter(SimpleIterator(5))



print(next(next(simple_iter)))
print(next(next(simple_iter)))
print(next(next(simple_iter)))