class Solution:
    def sumOfBeauties(self, nums) -> int:
        length = len(nums)

        prefixSum = [0] * length
        prefixSum[0] = nums[0]

        for i in range(1, length):
            prefixSum[i] = max(prefixSum[i - 1], nums[i])

        suffixSum = [0] * length
        suffixSum[-1] = nums[-1]

        for i in reversed(range(length - 1)):
            suffixSum[i] = min(suffixSum[i + 1], nums[i])

        result = 0
        for i in range(1, length - 1):
            if prefixSum[i - 1] < nums[i] and nums[i] < suffixSum[i + 1]:
                result += 2
            elif nums[i - 1] < nums[i] and nums[i] < nums[i + 1]:
                result += 1

        return result

solution = Solution()
print(solution.sumOfBeauties([1, 2, 3]))
print(solution.sumOfBeauties([2, 4, 6, 4]))
