class Solution:
    def anagramMappings(self, nums1, nums2):
        result = []
        mapping = {}

        for j in range(len(nums2)):
            mapping[nums2[j]] = j
        
        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        
        return result

solution = Solution()
print(solution.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
print(solution.anagramMappings([84, 46], [84, 46]))