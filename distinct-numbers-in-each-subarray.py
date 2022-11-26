from collections import Counter

class Solution:
    def distinctNumbers(self, nums, k: int):
        result = []
        
        counter = Counter()

        for i in range(k):
            counter[nums[i]] += 1
        
        result.append(len(counter.keys()))
        current = set(nums[:k])

        for i in range(k, len(nums)):
            counter[nums[i]] += 1
            counter[nums[i - k]] -= 1
            
            current.add(nums[i])
            
            if counter[nums[i - k]] == 0:
                current.discard(nums[i - k])
            
            result.append(len(current))

        return result

solution = Solution()
assert solution.distinctNumbers([1, 2, 3, 2, 2, 1, 3], 3) == [3, 2, 2, 2, 3]
assert solution.distinctNumbers([1, 1, 1, 1, 2, 3, 4], 4) == [1, 2, 3, 4]