import bisect
from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict):
        self.indecies = defaultdict(list)
        
        for i in range(len(wordsDict)):
            self.indecies[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        if not word1 in self.indecies:
            return -1
        if not word2 in self.indecies:
            return -1

        a = self.indecies[word1]
        b = self.indecies[word2]

        if len(a) == len(b) == 1:
            return abs(a[0] - b[0])

        if len(a) > len(b):
            a, b = b, a

        minimum = float('inf')

        for i in a:
            index = bisect.bisect_left(b, i)
            if index == 0:
                minimum = min(minimum, abs(i - b[index]))
            elif index == len(b):
                minimum = min(minimum, abs(i - b[index - 1]))
            else:
                minimum = min(minimum, abs(i - b[index]))
                minimum = min(minimum, abs(i - b[index - 1]))

        return minimum

solution = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
assert solution.shortest("coding", "practice") == 3
assert solution.shortest("makes", "coding") == 1