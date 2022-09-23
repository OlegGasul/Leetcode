class MyHashMap:

    def __init__(self):
        self.nums = [-1] * (10 ** 6 + 1)
        
    def put(self, key: int, value: int) -> None:
        self.nums[key] = value

    def get(self, key: int) -> int:
        return self.nums[key]

    def remove(self, key: int) -> None:
        self.nums[key] = -1

hashMap = MyHashMap()
hashMap.put(1, 10)
hashMap.put(2, 100)
print(hashMap.get(1))
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))