import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        length = len(self.nums)
        if length % 2 == 0:
            return (self.nums[length // 2] + self.nums[length // 2 - 1]) / 2
        else:
            return self.nums[length // 2]

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())