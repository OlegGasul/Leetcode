class Solution:
    def sumOfThree(self, num: int):
        if num % 3 != 0:
            return []
        
        second = num // 3
        return [second - 1, second, second + 1]

solution = Solution()
print(solution.sumOfThree(33))
print(solution.sumOfThree(66))
print(solution.sumOfThree(48))
print(solution.sumOfThree(4))
print(solution.sumOfThree(50))