def singleNumber(nums):
    s = set()
    
    for x in nums:
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    return list(s)

print(singleNumber([1, 2, 1, 3, 2, 5]))