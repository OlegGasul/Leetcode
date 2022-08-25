def intersect(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    result = []

    while nums1 and nums2:
        if nums1[0] == nums2[0]:
            result.append(nums1.pop(0))
            nums2.pop(0)
        elif nums1[0] < nums2[0]:
            nums1.pop(0)
        else:
            nums2.pop(0)

    return result

print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))