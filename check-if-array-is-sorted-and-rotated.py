class Solution:
    def check(self, nums) -> bool:
        pivotFound = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if pivotFound:
                    return False
                pivotFound = True

        if pivotFound and nums[-1] > nums[0]:
            return False

        return True

solution = Solution()
print(solution.check([3, 4, 5, 1, 2]))
print(solution.check([2, 1, 3, 4]))
print(solution.check([1, 2, 3]))