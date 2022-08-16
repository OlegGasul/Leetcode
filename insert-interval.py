# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
#
# Input: intervals = [[3,5],[12,16]], newInterval = [1,2]
# Output: [[1,2],[3,5],[12,16]]


def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    
    if len(newInterval) == 0:
        return intervals
    
    for i, interval in enumerate(intervals):
        if newInterval[1] < interval[0]:
            intervals.insert(i, newInterval)
            return intervals
        
        if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
            interval[0] = min(interval[0], newInterval[0])
            interval[1] = max(interval[1], newInterval[1])
            
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] > interval[1]:
                    return intervals
                interval[1] = max(interval[1], intervals[j][1])
                intervals.pop(j)

            return intervals

    intervals.append(newInterval)
                
    return intervals
        
        
# [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# [[1,2],[3,8],[6,7],[8,10],[12,16]]
# [[1,2],[3,8],[8,10],[12,16]]
# [[1,2],[3,10],[12,16]]

print(insert([[1,3],[6,9]], [2,5]))
print(insert([[3,5],[12,16]], [1,2]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(insert([], [2,5]))
print(insert([[1,5]], [6,8]))
print(insert([[1,5]], [0,3]))
print(insert([[1,5]], [0,0]))