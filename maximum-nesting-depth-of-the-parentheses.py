class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        current = 0
        
        for ch in s:
            if ch == "(":
                current += 1
            elif ch == ")":
                current -= 1
                
            result = max(result, current)
            
        return result

solution = Solution()
print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
print(solution.maxDepth("(1)+((2))+(((3)))"))