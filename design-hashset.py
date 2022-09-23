class MyHashSet:

    def __init__(self):
        self.nums = 0

    def add(self, key: int) -> None:
        self.nums |= (1 << key)

    def remove(self, key: int) -> None:
        self.nums &= ~(1 << key)
    
    def contains(self, key: int) -> bool:
        return self.nums & (1 << key) > 0

myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))