def findDifference(nums1, nums2):
    numSet1 = set(nums1)
    numSet2 = set(nums2)
        
    return [list(numSet1 - numSet2), list(numSet2 - numSet1)]

print(findDifference([1, 2, 3], [2, 4, 6]))
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))