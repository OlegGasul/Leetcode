class Solution:
    def distinctAverages(self, nums) -> int:
        nums.sort()

        result = set()
        while nums:
            result.add((nums.pop(0) + nums.pop()) / 2)
        
        return len(result)

solution = Solution()
assert solution.distinctAverages([4, 1, 4, 0, 3, 5]) == 2
assert solution.distinctAverages([1, 100]) == 1