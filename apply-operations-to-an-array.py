class Solution:
    def applyOperations(self, nums):
        length = len(nums)
        nonZeros = []

        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
            if nums[i] != 0:
                nonZeros.append(nums[i])

        nonZeros.append(nums[-1])
        nonZeros += [0] * (length - len(nonZeros))

        return nonZeros

solution = Solution()
print(solution.applyOperations([1, 2, 2, 1, 1, 0]))
print(solution.applyOperations([0, 1]))