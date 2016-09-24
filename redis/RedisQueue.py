import redis

class RedisQueue(object):

    def __init__(self, name, namespace='queue', **redis_kwargs):
        self.__db = redis.Redis(host='127.0.0.1', port=6379, db=0)
        self.key = '%s:%s' % (namespace, name)

    def qsize(self):
        return self.__db.llen(self.key)

    def empty(self):
        return self.qsize == 0

    def put(self, item):
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        if block:
            print self.__db.keys()
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        return self.get(False)