class Solution:
    def countHillValley(self, nums) -> int:
        if len(nums) < 3:
            return 0
        
        prev = nums[0]
        result = 0

        for i in range(1, len(nums) - 1):
            if nums[i] ==  nums[i + 1]:
                continue
            
            if nums[i] > prev and nums[i] > nums[i + 1]:
                result += 1
            elif nums[i] < prev and nums[i] < nums[i + 1]:
                result += 1
            
            prev = nums[i]
        
        return result

solution = Solution()
assert solution.countHillValley([2, 4, 1, 1, 6, 5]) == 3
assert solution.countHillValley([6, 6, 5, 5, 4, 1]) == 0