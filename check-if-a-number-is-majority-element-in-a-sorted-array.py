import bisect

class Solution:
    def isMajorityElement(self, nums, target: int) -> bool:
        if not nums:
            return False
        
        length = len(nums)
        if nums[length // 2] != target:
            return False

        a = bisect.bisect_left(nums, target)
        if a >= length or nums[a] != target:
            return False
        b = bisect.bisect_right(nums, target)

        return b - a > len(nums) / 2

solution = Solution()
assert solution.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5) == True
assert solution.isMajorityElement([10, 100, 101, 101], 101) == False