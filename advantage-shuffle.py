import bisect

def advantageCount(nums1, nums2):
    nums1.sort()
    result = []
        
    for num in nums2:
        index = bisect.bisect_right(nums1, num)
        if index < len(nums1):
            result.append(nums1.pop(index))
        else:
            result.append(nums1.pop(0))
                
    return result

print(advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
print(advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))