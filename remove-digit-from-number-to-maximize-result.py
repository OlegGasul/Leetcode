class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = float('-inf')
        
        for i in range(len(number)):
            if number[i] == digit:
                result = max(result, int(number[:i] + number[i + 1:]))
                
        return str(result)

solution = Solution()
print(solution.removeDigit("123", "3"))