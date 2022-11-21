import math

class Solution:
    def isGoodArray(self, nums) -> bool:
        if len(nums) == 1:
            return nums[0] == 1

        a = nums[0]

        for i in range(1, len(nums)):
            if math.gcd(a, nums[i]) == 1:
                return True
            a = math.gcd(a, nums[i])

        return False

solution = Solution()
print(solution.isGoodArray([12, 5, 7, 23]))
print(solution.isGoodArray([29, 6, 10]))
print(solution.isGoodArray([3, 6]))