import heapq

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule) :
        pq = []

        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(pq, [interval.start, interval.end])
        
        result = []

        a, b = heapq.heappop(pq)

        while pq:
            c, d = heapq.heappop(pq)

            if c > b:
                result.append(Interval(b, c))
            b = max(b, d)
        
        return result

def makeIntervals(arr):
    result = []
    
    for ints in arr:
        current = []
        for start, end in ints:
            current.append(Interval(start, end))
        
        result.append(current)
    
    return result

def printIntervals(intervals):
    for interval in intervals:
        print('[' + str(interval.start) + ', ' + str(interval.end) + ']')
    
    print()

solution = Solution()
printIntervals(solution.employeeFreeTime(makeIntervals([[[1,2],[5,6]],[[1,3]],[[4,10]]])))
printIntervals(solution.employeeFreeTime(makeIntervals([[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]])))
