class Fibonacci(object):
    data_list = list()
    fibonacci_list = [1, 2]

    def __init__(self, n):
        self.n = n
        for i in range(0, self.n):
            self.data_list.append(i)
        print("---init---", self.data_list)
        for j in self.data_list:
            if j == 0:
                self.fibonacci_list = [0]
            elif j == 1:
                self.fibonacci_list = [0, 1]
            elif j >= 2:
                fn = self.fibonacci_list[j - 1] + self.fibonacci_list[j - 2]
                self.fibonacci_list.append(fn)
        print("---init---", self.fibonacci_list)

    def __str__(self):
        return str(self.fibonacci_list)

    def __iter__(self):
        return IterFibonacci(self)


class IterFibonacci(object):
    def __init__(self, obj):
        self.obj = obj
        self.i = 0

    def __iter__(self):
        pass

    def __next__(self):
        while self.i < len(self.obj.fibonacci_list):
            rtn = self.obj.fibonacci_list[self.i]
            self.i += 1
            return rtn
        else:
            raise StopIteration


fibonacci_test = Fibonacci(15)
print(fibonacci_test)
for i in fibonacci_test:
    print(i)
