import collections

def divideArray(nums) -> bool:
    if len(nums) % 2 == 1:
        return False
    
    counter = collections.Counter(nums)
    for x in counter.values():
        if x % 2 == 1:
            return False

    return True

print(divideArray([3, 2, 3, 2, 2, 2]))
print(divideArray([1, 2, 3, 4]))
