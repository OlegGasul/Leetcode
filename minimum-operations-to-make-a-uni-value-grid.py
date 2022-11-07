class Solution:
    def minOperations(self, grid, x: int) -> int:
        nums = []
        for row in grid:
            nums += row

        modval = nums[0] % x
        if not all(v % x == modval for v in nums):
            return -1
        
        nums.sort()
        midval = nums[len(nums) // 2]
        
        return sum(abs(midval - v) for v in nums) // x

solution = Solution()
print(solution.minOperations([[2, 4], [6, 8]], 2))
print(solution.minOperations([[1, 5], [2, 3]], 1))