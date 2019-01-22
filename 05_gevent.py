import gevent
import time

from gevent import monkey

monkey.patch_all()


def demo_1():
    while True:
        print("----------1----------")
        time.sleep(1)


def demo_2():
    while True:
        print("----------2---------")
        time.sleep(1)


gevent.joinall([
    gevent.spawn(demo_1),
    gevent.spawn(demo_2)
])
