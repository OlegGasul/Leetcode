import functools
import heapq

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        def compare(a, b):
            return a[1] - b[1] if a[0] == b[0] else a[0] - b[0]

        intervals = sorted(intervals, key = functools.cmp_to_key(compare))
        
        pq = []
        heapq.heappush(pq, intervals[0][1])

        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, b)

        return len(pq)

solution = Solution()
print(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(solution.minMeetingRooms([[7, 10], [2, 4]]))