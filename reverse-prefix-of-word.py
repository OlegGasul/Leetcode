class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        letters = list(word)
        
        for i in range(len(letters)):
            if letters[i] == ch:
                return ''.join(letters[: i + 1][::-1] + letters[i + 1 :])
            
        return word

solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))
print(solution.reversePrefix("xyxzxe", "z"))