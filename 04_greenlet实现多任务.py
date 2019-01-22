import greenlet
import time


def demo_1():
    while True:
        gr2.switch()
        print("---1.1---")
        print("---1---")
        time.sleep(1)


def demo_2():
    while True:
        gr1.switch()
        print("---2.1---")
        print("---2--")
        time.sleep(1)


gr1 = greenlet.greenlet(demo_1)
gr2 = greenlet.greenlet(demo_2)

gr1.switch()
