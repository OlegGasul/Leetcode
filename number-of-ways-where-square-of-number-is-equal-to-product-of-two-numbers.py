from collections import Counter

class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        squares1 = Counter()
        for num in nums1:
            squares1[num * num] += 1
            
        squares2 = Counter()
        for num in nums2:
            squares2[num * num] += 1
            
        result = 0
        
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                result += squares2[nums1[i] * nums1[j]]
                
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                result += squares1[nums2[i] * nums2[j]]
                
        return result

solution = Solution()
print(solution.numTriplets([7, 4], [5, 2, 8, 9]))