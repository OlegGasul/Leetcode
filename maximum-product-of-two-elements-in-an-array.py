class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 2:
            return (nums[0] - 1) * (nums[1] - 1)

        maxes = [float('-inf'), float('-inf')]

        for n in nums:
            if n > maxes[1]:
                temp = maxes[1]
                maxes[1] = n
                if temp > maxes[0]:
                    maxes[0] = temp
            elif n > maxes[0]:
                maxes[0] = n

        return (maxes[0] - 1) * (maxes[1] - 1)

solution = Solution()
print(solution.maxProduct([3, 4, 5, 2]))
print(solution.maxProduct([1, 5, 4, 5]))
print(solution.maxProduct([3, 7]))