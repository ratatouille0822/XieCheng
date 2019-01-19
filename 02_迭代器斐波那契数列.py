class Fibonacci(object):

    data_list = [1, 2]

    def __init__(self, n):
        self.n = n

    def __str__(self):
        if self.n == 1:
            return [1]
        elif self.n == 2:
            return [1, 2]
        elif self.n >= 3:
            while len(self.data_list) < self.n:
                self.data_list.append()


        return self.Fibonacci

    def __iter__(self):
        return IterFibonacci(self)




class IterFibonacci(object):
    def __init__(self, obj):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass









if __name__ == "__main__":
    main()