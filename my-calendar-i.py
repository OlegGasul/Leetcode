from sortedcontainers import SortedList
import bisect

class MyCalendar:

    def __init__(self):
        self.intervals = SortedList()

    def book(self, start: int, end: int) -> bool:
        if len(self.intervals) == 0:
            self.intervals.add(start)
            self.intervals.add(end)
            return True
        
        insertIndex = bisect.bisect_right(self.intervals, start)
        if insertIndex != bisect.bisect_left(self.intervals, end) or insertIndex % 2 != 0:
            return False
        
        if insertIndex == len(self.intervals):
            self.intervals.add(start)
            self.intervals.add(end)
        else:
            self.intervals.add(end)
            self.intervals.add(start)
        
        return True

myCalendar = MyCalendar()
assert myCalendar.book(10, 20)
assert myCalendar.book(15, 25) == False
assert myCalendar.book(20, 30)
assert myCalendar.book(1, 2)