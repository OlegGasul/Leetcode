class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        
        diff = (bobSum - aliceSum) // 2
        
        bobSizes = set(bobSizes)
        
        for size in aliceSizes:
            if size + diff in bobSizes:
                return [size, size + diff]
            
        return []

solution = Solution()
print(solution.fairCandySwap([1, 1], [2, 2]))
print(solution.fairCandySwap([1, 2], [2, 3]))
print(solution.fairCandySwap([2], [1, 3]))