class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        suffixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i] = prefixSum[i - 1] + nums[i] if nums[i] == 1 else 0
            suffixSum[n - i - 1] = suffixSum[n - i] + nums[n - i - 1] if nums[n - i - 1] == 1 else 0

        result = float('-inf')
        for i in range(n):
            if nums[i] == 0:
                result = max(result, prefixSum[i - 1] + suffixSum[i + 1] + 1)

        return max(result, max(prefixSum), max(suffixSum))

solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))