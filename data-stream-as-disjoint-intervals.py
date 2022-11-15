from collections import deque

class SummaryRanges:

    def __init__(self):
        self.ranges = deque([])

    def insertIntoRange(self, value: int):
        if not self.ranges:
            self.ranges.append([value, value])
            return
        
        left = 0
        right = len(self.ranges) - 1

        while left < right:
            middle = left + (right - left) // 2
            
            a, b = self.ranges[middle]

            if value >= a and value <= b:
                return

            if value < a:
                right = middle - 1
                if right < 0:
                    right = 0
                    break
            else:
                left = middle + 1
                if left > len(self.ranges) - 1:
                    left = len(self.ranges) - 1
                    break;

        middle = left + (right - left) // 2
        a, b = self.ranges[middle]

        if value >= a and value <= b:
            return

        if value <= a:
            if value == a - 1:
                self.ranges[middle] = [value, b]
                a = value
            else:
                self.ranges.insert(middle, [value, value])
                a = value
                b = value
            
            if middle > 0:
                a1, b1 = self.ranges[middle - 1]
                if a - 1 <= b1:
                    self.ranges[middle - 1] = [a1, b]
                    del self.ranges[middle]

        elif value >= b:
            if value == b + 1:
                self.ranges[middle] = [a, value]
                b = value
            else:
                middle += 1
                self.ranges.insert(middle, [value, value])
                a = value
                b = value
            
            if middle < len(self.ranges) - 1:
                a1, b1 = self.ranges[middle + 1]
                if b + 1 >= a1:
                    self.ranges[middle] = [a, b1]
                    del self.ranges[middle + 1]

    def addNum(self, value: int) -> None:
        self.insertIntoRange(value)

    def getIntervals(self):
        return list(self.ranges)
        

def process(operations):
    for op in operations:
        if not op:
            print(summaryRanges.getIntervals())
        else:
            summaryRanges.addNum(op[0])

summaryRanges = SummaryRanges()
process([[], [3], [], [4], [], [7], [], [1], [], [0], [], [1], [], [2], []])
process([
    [],[49],[],[97],[],[53],[],[5],[],[33],[],[65],[],[62],[],[51],[],[100],[],[38],[],[61],[],[45],[],[74],
    [],[27],[],[64],[],[17],[],[36],[],[17],[],[96],[],[12],[],[79],[],[32],[],[68],[],[90],[],[77],[],[18],
    [],[39],[],[12],[],[93],[],[9],[],[87],[],[42],[],[60],[],[71],[],[12],[],[45],[],[55],[],[40],[],[78],
    [],[81],[],[26],[],[70],[],[61],[],[56],[],[66],[],[33],[],[7],[],[70],[],[1],[],[11],[],[92],[],[51],
    [],[90],[],[100],[],[85],[],[80],[],[0],[],[78],[],[63],[],[42],[],[31],[],[93],[],[41],[],[90],[],[8],
    [],[24],[],[72],[],[28],[],[30],[],[18],[],[69],[],[57],[],[11],[],[10],[],[40],[],[65],[],[62],[],[13],
    [],[38],[],[70],[],[37],[],[90],[],[15],[],[70],[],[42],[],[69],[],[26],[],[77],[],[70],[],[75],[],[36],
    [],[56],[],[11],[],[76],[],[49],[],[40],[],[73],[],[30],[],[37],[],[23],[]])
