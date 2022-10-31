class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        result = 1
        
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                result += 1
                
        return result

solution = Solution()
print(solution.commonFactors(12, 6))
print(solution.commonFactors(7, 5))