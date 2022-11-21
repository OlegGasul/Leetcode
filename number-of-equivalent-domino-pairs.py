from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        counter = Counter()

        result = 0

        for a, b in dominoes:
            if (a, b) in counter:
                result += counter[(a, b)]
            if a != b and (b, a) in counter:
                result += counter[(b, a)]
            
            counter[(a, b)] += 1

        return result

solution = Solution()
assert solution.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
assert solution.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3