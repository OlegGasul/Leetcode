from sortedcontainers import SortedSet

class Solution:
    def maxChunksToSorted(self, arr) -> int:
        sortedSet = SortedSet(arr)

        current = SortedSet()
        result = 0

        for i in range(len(arr)):
            current.add(arr[i])
            if list(current) == list(sortedSet[ : i + 1]):
                result += 1
        
        return result

solution = Solution()
assert solution.maxChunksToSorted([4, 3, 2, 1, 0]) == 1
assert solution.maxChunksToSorted([1, 0, 2, 3, 4]) == 4