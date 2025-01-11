from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self._cache.get(key)
        if value is None:
            value = -1
        else:
            self._cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        self._cache[key] = value
        self._cache.move_to_end(key)
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)