from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = frozenset(wordDict)

        @lru_cache
        def canMake(start):
            if start >= len(s):
                return True
            
            for i in range(start, len(s)):
                if s[start : i + 1] in wordDict:
                    result = canMake(i + 1)
                    if result:
                        return True

            return False

        return canMake(0)

solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))
print(solution.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
