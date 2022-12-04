class Solution:
    def minimumAverageDifference(self, nums) -> int:
        minimum = float('inf')

        n = len(nums)
        prefixSum = [0] * (n + 1)
        suffixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
            suffixSum[n - i - 1] = suffixSum[n - i] + nums[n - i - 1]

        result = 0

        for i in range(n):
            a = prefixSum[i] // (i + 1)
            if i < n - 1:
                b = suffixSum[i + 1] // (n - (i + 1))
            else:
                b = 0
            
            c = abs(a - b)
            
            if c < minimum:
                minimum = c
                result = i

        return result

solution = Solution()
assert solution.minimumAverageDifference([2, 5, 3, 9, 5, 3]) == 3
assert solution.minimumAverageDifference([0]) == 0