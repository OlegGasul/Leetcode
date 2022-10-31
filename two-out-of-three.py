def twoOutOfThree(nums1, nums2, nums3):
    nums1 = set(nums1)
    nums2 = set(nums2)
    nums3 = set(nums3)
        
    result = set()
        
    result.update(nums1.intersection(nums2))
    result.update(nums1.intersection(nums3))
    result.update(nums2.intersection(nums3))
        
    return list(result)

print(twoOutOfThree([1, 1, 3, 2], [2, 3], [3]))