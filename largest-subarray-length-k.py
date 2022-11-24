class Solution:
    def largestSubarray(self, nums, k: int):
        maximum = 0
        maximumIndex = -1

        for i in range(len(nums) - k + 1):
            if nums[i] > maximum:
                maximum = nums[i]
                maximumIndex = i
        
        return nums[maximumIndex : maximumIndex + k]

solution = Solution()
print(solution.largestSubarray([1, 4, 5, 2, 3], 3))
print(solution.largestSubarray([1, 4, 5, 2, 3], 4))
print(solution.largestSubarray([1, 4, 5, 2, 3], 4))