import functools

class Solution:
    def merge(self, intervals):
        def compare(a, b):
            if a[0] == b[0]:
                return a[1] - b[1]
            else:
                return a[0] - b[0]
        
        intervals = sorted(intervals, key = functools.cmp_to_key(compare))

        i = 1
        a, b = intervals[0]

        while i < len(intervals):
            c, d = intervals[i]
            
            if c <= b:
                intervals[i - 1][1] = max(b, d)
                b = intervals[i - 1][1]
                intervals.pop(i)
            else:
                a, b = intervals[i]
                i += 1

        return intervals

solution = Solution()
assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert solution.merge([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]) == [[1, 3], [4, 7]]