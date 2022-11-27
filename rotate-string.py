class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        
        for i in range(1, len(s)):
            if s[i :] + s[ : i] == goal:
                return True
        
        return False

solution = Solution()
assert solution.rotateString("abcde", "cdeab") == True
assert solution.rotateString("abcde", "abced") == False
assert solution.rotateString("abcde", "cde") == False