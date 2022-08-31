import functools

def largestInteger(num: int) -> int:
    nums = [int(x) for x in list(str(num))]
        
    length = len(nums)
    evens = []
    evensIndexes = []
    odds = []
    oddsIndexes = []

    for i in range(length):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
            evensIndexes.append(i)
        else:
            odds.append(nums[i])
            oddsIndexes.append(i)

    evens.sort(reverse = True)
    evensIndexes.sort()
    odds.sort(reverse = True)
    oddsIndexes.sort()

    for i in range(len(evens)):
        nums[evensIndexes[i]] = evens[i]

    for i in range(len(odds)):
        nums[oddsIndexes[i]] = odds[i]

    return int(''.join([str(x) for x in nums]))

print(largestInteger(1234))
print(largestInteger(65875))