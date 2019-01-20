class Fibonacci(object):
    fibonacci_list = list()
    a = 0
    b = 1

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.fibonacci_list) < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.fibonacci_list.append(self.b)
            return self.a
        else:
            raise StopIteration


fibonacci_test = Fibonacci(10)
print(fibonacci_test)
for i in fibonacci_test:
    print(i)