import bisect
from collections import defaultdict

class Solution:
    def shortestWordDistance(self, wordsDict, word1: str, word2: str) -> int:
        a = []
        b = []

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                a.append(i)
            if wordsDict[i] == word2:
                b.append(i)

        result = float('inf')
        if word1 == word2:
            for i in range(1, len(a)):
                result = min(result, a[i] - a[i - 1])
            return result

        if len(a) == len(b) == 1:
            return abs(a[0] - b[0])
        
        if len(a) > len(b):
            a, b = b, a

        for i in a:
            index = bisect.bisect_left(b, i)
            if index == 0:
                result = min(result, abs(i - b[index]))
            elif index == len(b):
                result = min(result, abs(i - b[index - 1]))
            else:
                result = min(result, abs(i - b[index]))
                result = min(result, abs(i - b[index - 1]))

        return result

solution = Solution()
assert solution.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1
assert solution.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes") == 3