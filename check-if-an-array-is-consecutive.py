class Solution:
    def isConsecutive(self, nums) -> bool:
        return max(nums) - min(nums) + 1 == len(nums) == len(set(nums))

solution = Solution()
print(solution.isConsecutive([1, 3, 4, 2]))
print(solution.isConsecutive([1, 3]))
print(solution.isConsecutive([0, 3, 0, 3]))