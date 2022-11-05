class Solution:
    def findLonely(self, nums):
        nums.sort()

        result = []

        for i in range(len(nums)):
            if (i == 0 or nums[i - 1] < nums[i] - 1) and (i == len(nums) - 1 or nums[i + 1] > nums[i] + 1):
                result.append(nums[i])
        
        return result

solution = Solution()
print(solution.findLonely([10, 6, 5, 8]))
print(solution.findLonely([1, 3, 5, 3]))