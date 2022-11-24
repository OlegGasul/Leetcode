class Solution:
    def sumOfDigits(self, nums) -> int:
        num = min(nums)

        result = 0
        while num:
            result += num % 10
            num //= 10
        
        return 1 if result % 2 == 0 else 0

solution = Solution()
print(solution.sumOfDigits([34, 23, 1, 24, 75, 33, 54, 8]))
print(solution.sumOfDigits([99, 77, 33, 66, 55]))