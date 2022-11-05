class Solution:
    def rearrangeArray(self, nums):
        positive = 0
        negative = 1

        result = [0] * len(nums)

        for num in nums:
            if num > 0:
                result[positive] = num
                positive += 2
            else:
                result[negative] = num
                negative += 2

        return result

solution = Solution()
print(solution.rearrangeArray([3, 1, -2, -5, 2, -4]))
print(solution.rearrangeArray([-1, 1]))