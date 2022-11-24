import functools

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        if not intervals:
            return True
        
        def compare(a, b):
            return a[1] - b[1] if a[0] == b[0] else a[0] - b[0]

        intervals = sorted(intervals, key = functools.cmp_to_key(compare))

        for i in range(1, len(intervals)):
            a, b = intervals[i - 1]
            c, d = intervals[i]

            if c < b:
                return False
        
        return True

solution = Solution()
print(solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(solution.canAttendMeetings([[7, 10], [2, 4]]))