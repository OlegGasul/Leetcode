class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        required = (n * (n + 1)) // 2
        
        total = 0

        for num in nums:
            total += num
        
        return required - total

solution = Solution()
print(solution.missingNumber([3, 0, 1]))
print(solution.missingNumber([0, 1]))
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))