from collections import Counter

def fourSumCount(nums1, nums2, nums3, nums4) -> int:
    pairSums1 = Counter()
    
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            pairSums1[nums1[i] + nums2[j]] += 1
    
    result = 0

    for i in range(len(nums3)):
        for j in range(len(nums4)):
            result += pairSums1[- 1 * (nums3[i] + nums4[j])]
    
    return result



print(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))