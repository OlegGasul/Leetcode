class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        result = 1

        current = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
                result = max(result, current)
            else:
                current = 1

        return result

solution = Solution()
print(solution.findLengthOfLCIS([1, 3, 5, 4, 7]))
print(solution.findLengthOfLCIS([2, 2, 2, 2, 2]))