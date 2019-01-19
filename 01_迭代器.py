from collections import Iterable
from collections import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return IteratorClassmate(self)


class IteratorClassmate(object):
    def __init__(self, obj_from_class):
        self.obj = obj_from_class
        self.num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.obj.names):
            ret = self.obj.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration()


class_mate = Classmate()

class_mate.add("小明")
class_mate.add("小红")
class_mate.add("小黄")
class_mate.add("小兰")

iterator_classmate = iter(class_mate)

print("验证Classmate是否是可迭代类型：", isinstance(class_mate, Iterable))
print("验证IteratorClassmate是否是迭代器", isinstance(iterator_classmate, Iterator))

for names in class_mate:
    print(next(iterator_classmate))
    time.sleep(1)
