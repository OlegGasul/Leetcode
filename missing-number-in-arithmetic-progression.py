class Solution:
    def missingNumber(self, arr) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) / n
        expected = arr[0]

        for num in arr:
            if num != expected:
                return int(expected)
            expected += diff
        
        return int(expected)

solution = Solution()
assert solution.missingNumber([5, 7, 11, 13]) == 9
assert solution.missingNumber([15, 13, 12]) == 14