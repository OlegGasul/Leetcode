class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        count = 0
        
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                count += 1
            if count > 2:
                return False

        return True

solution = Solution()
assert solution.makePalindrome("abcdba") == True
assert solution.makePalindrome("abcdef") == False