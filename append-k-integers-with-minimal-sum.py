class Solution:
    def minimalKSum(self, nums, k: int) -> int:
        if k == 0:
            return 0
        
        result = 0

        nums.sort()
        nums = [0] + nums

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff <= 1:
                continue
            
            n = min(k, (nums[i] - nums[i - 1]) - 1)
            left = nums[i - 1] + 1
            right = nums[i - 1] + n
            result += (n / 2) * (left + right)
            k -= n

            if k == 0:
                return int(result)

        if k > 0:
            left = nums[-1] + 1
            right = nums[-1] + k
            result += (k / 2) * (left + right)

        return int(result)

solution = Solution()
print(solution.minimalKSum([1, 4, 25, 10, 25], 2))
print(solution.minimalKSum([5, 6], 6))