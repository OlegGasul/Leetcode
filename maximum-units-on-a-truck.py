class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])
        
        result = 0
        while truckSize and boxTypes:
            count, size = boxTypes.pop()
            canTake = min(truckSize, count)
            truckSize -= canTake
            result += canTake * size

        return result

solution = Solution()
assert solution.maximumUnits([[1, 3], [2, 2], [3, 1]], 4) == 8
assert solution.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91