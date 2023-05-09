import heapq

class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0
        
        visited = set()

        hq = []

        heapq.heappush(hq, [height[0], 0, 1])
        heapq.heappush(hq, [height[-1], length - 1, -1])

        visited.add(0)
        visited.add(length - 1)

        result = 0

        while hq:
            h, i, d = heapq.heappop(hq)
            newI = i + d
            
            if not newI in visited:
                result += max(0, h - height[newI])
                heapq.heappush(hq, [max(h, height[newI]), newI, d])
                visited.add(newI)

        return result

solution = Solution()
assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution.trap([4, 2, 0, 3, 2, 5]) == 9