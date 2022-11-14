class NumArray:

    def __init__(self, nums):
        self.prefixSum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right] - self.prefixSum[left - 1]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))