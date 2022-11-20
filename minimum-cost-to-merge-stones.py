from collections import deque

class Solution:
    def mergeStones(self, stones, k: int) -> int:
        if len(stones) < k:
            return -1
        
        prefixSum = deque([0] * (len(stones) + 1))

        for i in range(len(stones)):
            prefixSum[i] = prefixSum[i - 1] + stones[i]
        
        result = 0

        while len(prefixSum) > 2:
            if len(prefixSum) - 1 < k:
                return -1
            
            minIndex = -1
            minSum = float('inf')
            for i in range(k - 1, len(prefixSum) - 1):
                current = prefixSum[i] - prefixSum[i - k]
                if current < minSum:
                    minSum = current
                    minIndex = i

            index = minIndex - k + 1
            
            for _ in range(k):
                del prefixSum[index]
            prefixSum.insert(index, minSum + prefixSum[index - 1])

            result += minSum

        return result

solution = Solution()
print(solution.mergeStones([3, 2, 4, 1], 2))
print(solution.mergeStones([3, 2, 4, 1], 3))
print(solution.mergeStones([3, 5, 1, 2, 6], 3))
