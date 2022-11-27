class Solution:
    def countLetters(self, s: str) -> int:
        if not s:
            return 0
        
        result = 0

        prev = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                result += prev * (prev + 1) / 2
                prev = 1
            else:
                prev += 1
        
        result += prev * (prev + 1) / 2

        return int(result)

solution = Solution()
assert solution.countLetters("aaaba") == 8
assert solution.countLetters("aaaaaaaaaa") == 55