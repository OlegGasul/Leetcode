import heapq

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes) -> int:
        currentKeys = set()
        
        boxHeap = []
        for box in initialBoxes:
            heapq.heappush(boxHeap, [status[box] ^ 1, box])
        
        result = 0

        while boxHeap:
            closed, box = heapq.heappop(boxHeap)

            if closed == 1 and not box in currentKeys:
                break
            
            result += candies[box]
            currentKeys |= set(keys[box])
            
            for b in containedBoxes[box]:
                closed = 0 if status[b] == 1 or b in currentKeys else 1
                heapq.heappush(boxHeap, [closed, b])

        return result

solution = Solution()
assert solution.maxCandies([1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]) == 16