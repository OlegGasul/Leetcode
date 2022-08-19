import functools

def isIncluded(a, b):
    return a[0] >= b[0] and a[0] <= b[1] and a[1] >= b[0] and a[1] <= b[1]

def removeCoveredIntervals(intervals) -> int:
    length = len(intervals)
    if length < 2:
        return length
    
    def compare(a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]

    intervals = sorted(intervals, key = functools.cmp_to_key(compare))
    i = 1
    while i < len(intervals):
        prev = intervals[i - 1]
        curr = intervals[i]
        
        if isIncluded(curr, prev):
            intervals.pop(i)
        elif isIncluded(prev, curr):
            intervals.pop(i - 1)
        else:
            i += 1

    return len(intervals)

print(removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
# print(removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))