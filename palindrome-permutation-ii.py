from collections import Counter
from itertools import permutations

class Solution:
    def generatePalindromes(self, s: str):
        counter = Counter(s)

        hasOdd = False
        evens = []
        odd = None

        for value, count in counter.items():
            if count % 2 == 0:
                evens += [value] * (count // 2)
            else:
                if hasOdd:
                    return []
                hasOdd = True
                odd = value
        
        if odd:
            evens += [odd] * (counter[odd] // 2)

        result = []

        for values in list(permutations(evens)):
            values = list(values)
            result.append(''.join(values + ([odd] if odd else []) + list(reversed(values))))
            

        return list(set(result))

solution = Solution()
print(solution.generatePalindromes("aabb"))
print(solution.generatePalindromes("abc"))