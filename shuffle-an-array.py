import random
import copy

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def reset(self):
        return self.nums

    def shuffle(self):
        numsCopy = copy.copy(self.nums)
        random.shuffle(numsCopy)
        return numsCopy

    def shuffle2(self):
        numsCopy = copy.copy(self.nums)
        result = []
        
        while numsCopy:
            if len(numsCopy) > 1:
                result.append(numsCopy.pop(random.randrange(len(numsCopy) - 1)))
            else:
                result.append(numsCopy.pop())

        return result

solution = Solution([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(solution.shuffle())
print(solution.shuffle2())
print(solution.reset())