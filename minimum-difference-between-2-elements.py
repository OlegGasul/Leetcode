from sortedcontainers import SortedList

# https://leetcode.com/company/google/discuss/3711379/Google-L3-Interview-Question

class Solution:
    def findMinimumDifference(self, nums, k):
        sortedNums = SortedList()

        result = float('inf')

        for i in range(k, len(nums)):
            sortedNums.add(abs(nums[i - k]))
            value = abs(nums[i])
            index = sortedNums.bisect_left(value)
            
            if index > 0:
                result = min(result, abs((sortedNums[index - 1] - value)))
            if index <= len(sortedNums) - 1:
                result = min(result, abs((sortedNums[index] - value)))

        return result if result != float('inf') else -1

solution = Solution()
assert solution.findMinimumDifference([1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 6, 6, 6, 11, 11, 11, 11], 5) == 1
assert solution.findMinimumDifference([24, 1400, 1900, 1200, 98, 89, 123, 27], 2) == 3
