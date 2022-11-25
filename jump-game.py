class Solution:
    def canJump(self, nums) -> bool:
        steps = nums[0]

        i = 0
        while steps or i >= len(nums) - 1:
            if i + steps >= len(nums) - 1:
                return True
            
            maxJump = -1
            maxIndex = None
            for j in range(i + steps, i, -1):
                if j + nums[j] > maxJump:
                    maxJump = j + nums[j]
                    maxIndex = j

            i = maxIndex
            steps = nums[i]

        return False

solution = Solution()
assert solution.canJump([2, 3, 1, 1, 4]) == True
assert solution.canJump([3, 2, 1, 0, 4]) == False