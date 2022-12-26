class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        
        current = 0

        for i in range(len(nums) - 1):
            if nums[i] > current:
                current = nums[i]

            if current == 0:
                return False
            
            current -= 1
        
        return True

solution = Solution()
assert solution.canJump([2, 3, 1, 1, 4]) == True
assert solution.canJump([3, 2, 1, 0, 4]) == False