def singleNumber(nums) -> int:
    elements = set()

    for x in nums:
        if x in elements:
            elements.remove(x)
        else:
            elements.add(x)

    return list(elements).pop()

print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))