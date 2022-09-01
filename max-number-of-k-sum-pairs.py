from collections import Counter

def maxOperations(nums, k: int) -> int:
    counter = Counter()
        
    result = 0
        
    for i in range(len(nums)):
        value = k - nums[i]

        if value in counter:
            counter[value] -= 1
            if counter[value] == 0:
                del counter[value]
            result += 1
        else:
            counter[nums[i]] += 1

    return result

print(maxOperations([1, 2, 3, 4], 5))
print(maxOperations([3, 1, 3, 4, 3], 6))
print(maxOperations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3))