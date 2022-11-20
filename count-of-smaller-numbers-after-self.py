from collections import deque
import bisect

class Solution:
    def countSmaller(self, nums):
        dq = deque([])
        result = [0] * len(nums)
        
        i = len(nums) - 1
        while i >= 0:
            if len(dq) == 0:
                dq.append(nums[i])
            else:
                index = bisect.bisect_left(dq, nums[i])
                result[i] = index
                dq.insert(index, nums[i])

            i -= 1

        return result
            
solution = Solution()
assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
assert solution.countSmaller([-1]) == [0]
assert solution.countSmaller([-1, -1]) == [0, 0]