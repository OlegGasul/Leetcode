from functools import lru_cache, cmp_to_key
import bisect

class Solution:
    def smallestRange(self, nums):
        if len(nums) == 1:
            return [nums[0][0], nums[0][0]]

        def compare(a, b):
            return len(a) - len(b)

        for i in range(len(nums)):
            nums[i] = sorted(list(set(nums[i])))

        nums = sorted(nums, key = cmp_to_key(compare))

        @lru_cache
        def searchRange(index, a, b):
            if index >= len(nums):
                return a, b
            
            index1 = bisect.bisect_left(nums[index], a)
            index2 = bisect.bisect_left(nums[index], b)

            if index1 < index2:
                return searchRange(index + 1, a, b)
            
            if index1 == 0:
                b = nums[index][index1]
                return searchRange(index + 1, a, b)
            
            if index1 == len(nums[index]):
                a = nums[index][index1 - 1]
                return searchRange(index + 1, a, b)
            
            if nums[index][index1] == a or nums[index][index1] == b:
                return searchRange(index + 1, a, b)

            c = nums[index][index1 - 1]
            left = searchRange(index + 1, c, b)

            d = nums[index][index1]
            right = searchRange(index + 1, a, d)

            if left[1] - left[0] < right[1] - right[0]:
                return left
            else:
                return right
        
        a, b = float('-inf'), float('inf')

        for n in nums[0]:
            c, d = searchRange(1, n, n)
            if d - c < b - a:
                a, b = c, d

        return [a, b]

solution = Solution()
print(solution.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))