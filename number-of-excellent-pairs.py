from collections import Counter

class Solution:
    def countExcellentPairs(self, nums, k: int) -> int:
        counter = Counter(map(lambda n: n.bit_count(), set(nums)))
        return sum(counter[k1] * counter[k2] for k1 in counter for k2 in counter if k1 + k2 >= k)

solution = Solution()
assert solution.countExcellentPairs([1, 2, 3, 1], 3) == 5
assert solution.countExcellentPairs([5, 1, 1], 10) == 0