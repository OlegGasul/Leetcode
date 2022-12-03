import re

class Solution:
    def countSegments(self, s: str) -> int:
        return len(re.split('\s+', s))

solution = Solution()
assert solution.countSegments("Hello, my name is John") == 5
assert solution.countSegments("Hello") == 5