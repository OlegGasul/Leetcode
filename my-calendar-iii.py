from sortedcontainers import SortedList

class MyCalendarThree:

    def __init__(self):
        self.starts = SortedList([[0, 0]])
        self.result = 0

    def split(self, x: int) -> None:
        index = self.starts.bisect_left([x, 0])
        if index < len(self.starts) and self.starts[index][0] == x:
            return index
        
        self.starts.add([x, self.starts[index - 1][1]])

    def book(self, start: int, end: int) -> int:
        self.split(start)
        self.split(end)
        
        for interval in self.starts.irange([start, 0], [end, 0], (True, False)):
            interval[1] += 1
            self.result = max(self.result, interval[1])
        
        return self.result
        

solution = MyCalendarThree()
print(solution.book(10, 20))   # return 1
print(solution.book(50, 60))   # return 1
print(solution.book(10, 40))   # return 2
print(solution.book(5, 15))    # return 3
print(solution.book(5, 10))    # return 3
print(solution.book(25, 55))   # return 3

