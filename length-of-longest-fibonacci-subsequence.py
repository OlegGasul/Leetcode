def findIndex(nums, index, value):
    left = index
    right = len(nums) - 1

    while left < right:
        middle = left + (right - left) // 2

        if nums[middle] == value:
            return middle

        if nums[middle] > value:
            right = middle - 1
        else:
            left = middle + 1

    return left if left < len(nums) and nums[left] == value else -1

def countFibLength(nums, index, a, b, cache):
    counter = 0
    
    while index > 0:
        value = a + b
        
        index = findIndex(nums, index, value)

        if index > 0:
            counter += 1
            cache[(a, b)] = counter

            a = b
            b = value
            

    return counter


def lenLongestFibSubseq(nums) -> int:
    length = len(nums)

    maximum = 0

    cache = {}

    for i in range(length):
        for j in range(i + 1, length):
            if (nums[i], nums[j]) in cache:
                value = cache[(nums[i], nums[j])]
            else:
                value = countFibLength(nums, j + 1, nums[i], nums[j], cache)
            
            if value > 0:
                maximum = max(maximum, 2 + value)

            # print(cache)

    return maximum

def lenLongestFibSubseq2(nums: [int]) -> int:
    length = len(nums)
        
    values = set(nums)
    result = 0

    for i in range(length):
        for j in range(i + 1, length):
            a, b, counter = nums[i], nums[j], 2

            while a + b in values:
                counter += 1
                a, b = b, a + b
            result = max(result, counter)
    
    return 0 if result == 2 else result
            

print(lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
print(lenLongestFibSubseq2([1, 3, 7, 11, 12, 14, 18]))
print(lenLongestFibSubseq([1, 3, 5]))