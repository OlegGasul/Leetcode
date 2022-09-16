import bisect

class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.counter = 0

    def add(self, left: int, right: int) -> None:
        right += 1
        i = bisect.bisect_left(self.intervals, left)
        j = bisect.bisect_right(self.intervals, right)

        if i % 2 == 1:
            left = self.intervals[i - 1]
            i -= 1
            
        if j % 2 == 1:
            right = self.intervals[j]
            j += 1
            
        for k in range(i, j, 2):
             self.counter -= self.intervals[k + 1] - self.intervals[k]        
        
        self.counter += right - left
        self.intervals[i : j] = [left, right]
        
    def count(self) -> int:
        return self.counter

countIntervals = CountIntervals()
countIntervals.add(1, 5)
countIntervals.add(10, 15)
countIntervals.add(20, 25)
print(countIntervals.count())
countIntervals.add(6, 9)
print(countIntervals.count())
countIntervals.add(7, 11)
print(countIntervals.count())

# countIntervals = CountIntervals()
# countIntervals.add(1, 5)
# countIntervals.add(10, 15)
# print(countIntervals.count())
# countIntervals.add(20, 25)
# print(countIntervals.count())
# countIntervals.add(6, 9)
# print(countIntervals.count())
# countIntervals.add(11, 22)
# print(countIntervals.count())
# countIntervals.add(11, 26)
# print(countIntervals.count())

# countIntervals = CountIntervals()
# countIntervals.add(39, 44)
# countIntervals.add(13, 49)
# print(countIntervals.count())
# countIntervals.add(47, 50)

# countIntervals = CountIntervals()
# countIntervals.add(2, 3)
# countIntervals.add(7, 10)
# print(countIntervals.count())
# countIntervals.add(5, 8)
# print(countIntervals.count())
# countIntervals.add(1, 2)
# print(countIntervals.count())
# countIntervals.add(1, 10)
# print(countIntervals.count())
# countIntervals.add(12, 20)
# print(countIntervals.count())