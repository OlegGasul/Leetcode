from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))

        return any(count == Counter(str(1 << b)) for b in range(31))

solution = Solution()
assert solution.reorderedPowerOf2(1) == True
assert solution.reorderedPowerOf2(10) == False
assert solution.reorderedPowerOf2(24) == False
assert solution.reorderedPowerOf2(24222) == False
assert solution.reorderedPowerOf2(242111122) == False
assert solution.reorderedPowerOf2(215) == True
assert solution.reorderedPowerOf2(46) == True