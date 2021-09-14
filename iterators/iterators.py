class FiboIter:
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration
class FiboNumber:
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.n2 < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                self.n1 += 1
                return self.n2
            else:
                self.n1, self.n2 = self.n2, self.n1 + self.n2
                return self.n1
        else:
            raise StopIteration
class FibonacciIterator:
    def fibonacci_iterator_limit(limit): 
        fibonacci = FiboIter(limit)
        iterator_counter = 0
        for element in fibonacci:
            print(f"*   {iterator_counter}: {element}")
            iterator_counter += 1

    def fibonacci_number_limit(limit): 
        fibonacci_number_limit = FiboNumber(limit)
        time_of_iteration = 0
        for element in fibonacci_number_limit:
            print(f"*    {time_of_iteration}: {element}")
            time_of_iteration += 1  