def nextGreaterElement(nums1, nums2):
    stack = [0]
    greater = {}

    for i in reversed(range(len(nums2))):
        if nums2[i] > stack[-1]:
            while stack and nums2[i] > stack[-1]:
                stack.pop()

        if stack:
            greater[nums2[i]] = stack[-1]
        stack.append(nums2[i])

    for i in range(len(nums1)):
        nums1[i] = greater[nums1[i]] if nums1[i] in greater else -1

    return nums1

print(nextGreaterElement([4, 1, 2, 5, 7], [8, 3, 2, 4, 7, 1]))