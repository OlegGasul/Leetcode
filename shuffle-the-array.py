class Solution:
    def shuffle(self, nums, n: int):
        length = len(nums)
        middle = length // 2
        
        result = []

        for i in range(middle):
            result.append(nums[i])
            result.append(nums[middle + i])

        return result

solution = Solution()
print(solution.shuffle([2, 5, 1, 3, 4, 7], 3))
print(solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(solution.shuffle([1, 1, 2, 2], 2))