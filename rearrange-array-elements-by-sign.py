def rearrangeArray(nums):
    positives = []
    negatives = []

    for x in nums:
        if x > 0:
            positives.append(x)
        else:
            negatives.append(x)

    result = []
    for i in range(len(positives)):
        result.append(positives[i])
        result.append(negatives[i])

    return result

print(rearrangeArray([3, 1, -2, -5, 2, -4]))