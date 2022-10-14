import functools

def minInterval2(intervals, queries):
    cache = [float('inf')] * (10 ** 7 + 1)

    for left, right in intervals:
        size = right - left + 1

        for value in range(left, right + 1):
            cache[value] = min(cache[value], size)

    for i in range(len(queries)):
        result = cache[queries[i]]
        queries[i] = result if result < float('inf') else -1

    return queries

def minInterval(intervals, queries):
    def compare(a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]

    intervals = sorted(intervals, key = functools.cmp_to_key(compare))
    
    dp = []
    for i in range(len(queries)):
        dp.append([queries[i], i])

    dp = sorted(dp)

    result = [0] * len(queries)
    
    for i in range(len(dp)):
        query = dp[i][0]
        minimum = float('inf')
        
        j = 0
        while j < len(intervals):
            left, right = intervals[j]
            if query > right:
                intervals.pop(j)
                continue

            if query < left:
                break;

            if query >= left and query <= right:
                minimum = min(right - left + 1, minimum)

            j += 1

        result[dp[i][1]] = minimum if minimum < float('inf') else -1

    
    return result

print(minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]))
# print(minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))