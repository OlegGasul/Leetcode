from collections import defaultdict
import functools

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(set)

        for i in range(1, n + 1):
            digitsSum = sum([int(x) for x in list(str(i))])
            groups[digitsSum].add(i)
        
        def compare(a, b):
            return len(b) - len(a)

        result = 0
        length = None
        for g in sorted((groups.values()), key = functools.cmp_to_key(compare)):
            if not length:
                length = len(g)
            else:
                if len(g) < length:
                    break
            
            result += 1
        
        return result

solution = Solution()
assert solution.countLargestGroup(13) == 4
assert solution.countLargestGroup(2) == 2