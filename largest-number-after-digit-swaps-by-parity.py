import functools

def largestInteger(num: int) -> int:
    nums = [int(x) for x in list(str(num))]
    
    length = len(nums)
    evens = []
    odds = []
    
    for i in range(length):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
        else:
            odds.append(nums[i])

    evens.sort()
    odds.sort()

    for i in range(len(nums)):
        nums[i] = evens.pop() if nums[i] % 2 == 0 else odds.pop()

    return int(''.join([str(x) for x in nums]))

print(largestInteger(1234))
print(largestInteger(65875))