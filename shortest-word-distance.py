class Solution:
    def shortestDistance(self, wordsDict, word1: str, word2: str) -> int:
        a = None
        b = None

        result = float('inf')

        for i in range(len(wordsDict)):
            w = wordsDict[i]

            if w == word1:
                if b != None:
                    result = min(result, i - b)
                a = i
            elif w == word2:
                if a != None:
                    result = min(result, i - a)
                b = i

        return result

solution = Solution()
assert solution.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice") == 3