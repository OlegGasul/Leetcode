from collections import deque
import bisect

class Solution:
    def kEmptySlots(self, bulbs, k: int) -> int:
        q = deque([])
        days = 1
        
        for b in bulbs:
            if not q:
                q.append(b)
                days += 1
                continue
            
            index = bisect.bisect_left(q, b)
            q.insert(index, b)

            if index > 0:
                if q[index] - q[index - 1] - 1 == k:
                    return days
            if index < len(q) - 1:
                if q[index + 1] - q[index] - 1 == k:
                    return days
            
            days += 1

        return -1

solution = Solution()
assert solution.kEmptySlots([1, 3, 2], 1) == 2
assert solution.kEmptySlots([1, 2, 3], 1) == -1