import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.hq = []
        self.numSet = set()
        
        for num in range(1, 1001):
            heapq.heappush(self.hq, num)
            self.numSet.add(num)
        heapq.heapify(self.hq)

    def popSmallest(self) -> int:
        num = heapq.heappop(self.hq)
        self.numSet.discard(num)
        
        return num
        

    def addBack(self, num: int) -> None:
        if num in self.numSet:
            return
        
        heapq.heappush(self.hq, num)
        heapq.heapify(self.hq)

        
smallestInfiniteSet = SmallestInfiniteSet()
smallestInfiniteSet.addBack(2)
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())
smallestInfiniteSet.addBack(1)
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())
print(smallestInfiniteSet.popSmallest())