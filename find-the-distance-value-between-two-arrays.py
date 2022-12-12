import bisect

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        arr2.sort()

        result = 0
        
        for n in arr1:
            index = bisect.bisect_left(arr2, n)
            if index == 0:
                if abs(arr2[index] - n) > d:
                    result += 1
            elif index == len(arr2):
                if abs(arr2[index - 1] - n) > d:
                    result += 1
            else:
                if abs(arr2[index - 1] - n) > d and abs(arr2[index] - n) > d:
                    result += 1

        return result

solution = Solution()
assert solution.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2
assert solution.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3) == 2