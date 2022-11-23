from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums) -> int:
        counter = Counter(nums)

        for num in sorted(counter.keys(), reverse = True):
            if counter[num] == 1:
                return num

        return -1

solution = Solution()
assert solution.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]) == 8
assert solution.largestUniqueNumber([9, 9, 8, 8]) == -1