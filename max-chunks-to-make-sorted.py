class Solution:
    def maxChunksToSorted(self, arr) -> int:
        n = len(arr)
        minRight = [0] * (n + 1)
        maxLeft = [0] * (n + 1)
        minRight[-1] = arr[-1]

        for i in range(n):
            maxLeft[i] = max(maxLeft[i - 1], arr[i])
            minRight[n - i - 1] = min(minRight[n - i], arr[n - i - 1])

        result = 1
        for i in range(n - 1):
            if maxLeft[i] <= minRight[i + 1]:
                result += 1

        return result

solution = Solution()
assert solution.maxChunksToSorted([4, 3, 2, 1, 0]) == 1
assert solution.maxChunksToSorted([1, 0, 2, 3, 4]) == 4