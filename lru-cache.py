class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = []
        self.cache = {}

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        index = self.lru.remove(key)
        self.lru.append(key)
        
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        presentBefore = key in self.cache
        self.cache[key] = value

        if presentBefore:
            index = self.lru.remove(key)
            self.lru.append(key)
        else:
            self.lru.append(key)
            if len(self.lru) > self.capacity:
                keyToRemove = self.lru.pop(0)
                del self.cache[keyToRemove]
        
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
assert lru.get(1) == 1
lru.put(3, 3)
assert lru.get(2) == -1
lru.put(4, 4)
assert lru.get(1) == -1
assert lru.get(3) == 3
assert lru.get(4) == 4
