import itertools
import bisect

class Solution:
    def minWastedSpace(self, packages, boxes) -> int:
        packages.sort()
        prefixSum = list(itertools.accumulate([0] + packages))

        result = float('inf')

        for sizes in boxes:
            sizes.sort()
            
            if sizes[-1] < packages[-1]:
                continue
            
            current = 0
            prevIndex = 0

            for size in sizes:
                index = bisect.bisect_right(packages, size)
                prefix = prefixSum[index] - prefixSum[prevIndex]
                
                current += (index - prevIndex) * size - prefix
                if current > result:
                    break

                prevIndex = index
            
            result = min(result, current)

        if result == float('inf'):
            return -1

        return result % (10 ** 9 + 7)


solution = Solution()
print(solution.minWastedSpace([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]]))
print(solution.minWastedSpace([2, 3, 5], [[4, 8], [2, 8]]))