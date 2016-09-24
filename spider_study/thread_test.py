# coding=utf-8

from Queue import Queue
import random
import threading
import time


# 对于队列这个东西，可以说是必须要放进去几个才能取出来几个，队列会有等待效果，会一直等到放入取出才会结束

class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print "%s:%s is producing %d to the queue!\n" % (time.ctime(), self.getName(), i)
            self.data.put(i)
            time.sleep(5)
        print "%s:%s finished!" % (time.ctime(), self.getName())


class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(6):
            val = self.data.get()
            print "%s: %s is consuming. %d in the queue is consumed!\n" % (time.ctime(), self.getName(), val)
            # time.sleep(random.randrange(10))
        print "%s: %s finished!" % (time.ctime(), self.getName())


class ThreadJoin(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in xrange(10):
            print i


def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    consumer.join()
    producer.join()

    print 'All threads terminate!'

def main2():
    tj1 = ThreadJoin()
    tj2 = ThreadJoin()
    tj1.start()
    tj2.start()
    tj1.join()
    tj2.join()
    print 'i love you so much!!'

if __name__ == '__main__':
    # main()
    main2()