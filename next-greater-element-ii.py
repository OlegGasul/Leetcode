class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)

        stack = []
        result = [-1] * n

        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                num, j = stack.pop()
                result[j] = nums[i]

            stack.append([nums[i], i])

        if stack:
            for i in range(n):
                while stack and stack[-1][0] < nums[i]:
                    num, j = stack.pop()
                    result[j] = nums[i]

        return result

solution = Solution()
print(solution.nextGreaterElements([1, 2, 1]))
print(solution.nextGreaterElements([1, 2, 3, 4, 3]))