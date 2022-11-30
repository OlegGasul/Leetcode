class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        if start == destination:
            return 0
        
        if start > destination:
            start, destination = destination, start
        
        a = sum(distance[start : destination])
        b = sum(distance) - a

        return min(a, b)

solution = Solution()
assert solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 1) == 1
assert solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 2) == 3
assert solution.distanceBetweenBusStops([1, 2, 3, 4], 0, 3) == 4