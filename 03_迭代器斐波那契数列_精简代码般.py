class Fibonacci(object):
    # fibonacci_list = list()
    cnt = 0
    a = 0
    b = 1

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.cnt < self.n:
            self.a, self.b = self.b, self.a + self.b
            # self.fibonacci_list.append(self.b)
            self.cnt += 1
            return self.a
        else:
            raise StopIteration


fibonacci_test = Fibonacci(1)
print(fibonacci_test)
for i in fibonacci_test:
    print(i)
