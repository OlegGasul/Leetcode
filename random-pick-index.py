class Solution:

    def __init__(self, nums):
        self.indecies = {}

        for i in range(len(nums)):
            if not nums[i] in self.indecies:
                self.indecies[nums[i]] = [0, [i]]
            else:
                self.indecies[nums[i]][1].append(i)

    def pick(self, target: int) -> int:
        index = self.indecies[target][0]
        values = self.indecies[target][1]

        result = values[index]

        index += 1
        if index >= len(values):
            index = 0

        self.indecies[target][0] = index

        return result

solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(3))
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(1))