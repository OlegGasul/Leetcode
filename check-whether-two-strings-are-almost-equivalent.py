from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        
        for val in list((a - b).values()) + list((b - a).values()):
            if val > 3:
                return False
            
        return True

solution = Solution()
print(solution.checkAlmostEquivalent("aaaa", "bccb"))
print(solution.checkAlmostEquivalent("abcdeef", "abaaacc"))