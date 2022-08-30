def maxDistance(nums1, nums2) -> int:
    left = 0
    right = 0
    maximum = 0

    while left < len(nums1) and right < len(nums2):
        if nums1[left] <= nums2[right]:
            maximum = max(maximum, right - left)
            right += 1
        else:
            left += 1
            if left > right:
                right = left
    return maximum

print(maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
print(maxDistance([2, 2, 2], [10, 10, 1]))
print(maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))
print(maxDistance([5, 4], [3, 2]))