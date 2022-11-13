import bisect

class Solution:
    def findRadius(self, houses, heaters) -> int:
        houses.sort()
        heaters.sort()
        
        result = 0

        for i in range(len(houses)):
            index = bisect.bisect_left(heaters, houses[i])
            if index == 0:
                result = max(result, abs(houses[i] - heaters[index]))
            elif index == len(heaters):
                result = max(result, abs(houses[i] - heaters[index - 1]))
            else:
                result = max(result, min(abs(houses[i] - heaters[index - 1]), abs(houses[i] - heaters[index])))

        return result

solution = Solution()
print(solution.findRadius([1, 2, 3], [2]))
print(solution.findRadius([1, 2, 3, 4], [1, 4]))
print(solution.findRadius([1, 5], [2]))