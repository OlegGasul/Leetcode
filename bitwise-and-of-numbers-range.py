class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
           right = right & right - 1
        
        return right & left

solution = Solution()
print(solution.rangeBitwiseAnd(5, 7))
print(solution.rangeBitwiseAnd(0, 0))
print(solution.rangeBitwiseAnd(1, 2147483647))