import functools

# Timeout on large amount
def minGroups(intervals) -> int:
    if len(intervals) == 1:
        return 1
    
    def compare(a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]

    intervals = sorted(intervals, key = functools.cmp_to_key(compare))

    result = 0
    
    while intervals:
        result += 1

        newIntervals = []
        i = 1
        while i < len(intervals):
            prev = intervals[i - 1]
            interval = intervals[i]
            if interval[0] <= prev[1]:
                newIntervals.append(intervals.pop(i))
            else:
                i += 1

        intervals = newIntervals

    return result


print(minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
print(minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]))
