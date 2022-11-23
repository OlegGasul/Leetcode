class Solution:
    def isMajorityElement(self, nums, target: int) -> bool:
        if not nums:
            return False
        
        length = len(nums)

        i = 0
        while i < length and nums[i] < target:
            i += 1

        if i >= length:
            return False
        
        j = i
        while j < length and nums[j] == target:
            j += 1
        
        return j - i > length / 2

solution = Solution()
assert solution.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5) == True
assert solution.isMajorityElement([10, 100, 101, 101], 101) == False