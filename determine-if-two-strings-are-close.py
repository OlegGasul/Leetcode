from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)

        return sorted(a.values()) == sorted(b.values()) and set(word1) == set(word2)

solution = Solution()
assert solution.closeStrings("abc", "bca") == True
assert solution.closeStrings("a", "aa") == False
assert solution.closeStrings("cabbba", "abbccc") == True