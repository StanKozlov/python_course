class fibonacci_sequence:
    def __init__(self, i):
        self.m = 1
        self.n = 1
        self.i = i
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):        
        if self.count < self.i:
            ret_val = self.m
            self.m = self.n
            self.n += ret_val
            self.count += 1          
            return ret_val
        else:
            raise StopIteration('No more elements, my captain')

