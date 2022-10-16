import bisect

class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        bisect.insort_left(self.nums, val)
        return self.nums[len(self.nums) - self.k]

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))