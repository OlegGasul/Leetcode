class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indecies = {}
        for i in range(len(keyboard)):
            indecies[keyboard[i]] = i

        current = 0
        result = 0
        for ch in word:
            result += abs(indecies[ch] - current)
            current = indecies[ch]

        return result

solution = Solution()
assert solution.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba") == 4
assert solution.calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode") == 73