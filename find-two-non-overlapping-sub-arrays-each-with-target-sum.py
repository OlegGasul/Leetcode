from time import sleep
from functools import cmp_to_key

def minSumOfLengths(nums, target: int) -> int:
    length = len(nums)

    left = 0
    right = 0
    currentSum = nums[0]

    result = []

    while right < length:
        print()
        print('left = ' + str(left))
        print('right = ' + str(right))
        print('currentSum = ' + str(currentSum))

        if currentSum == target:
            result.append([left, right])
            print(result)

            if left < right:
                left += 1
                currentSum -= nums[left - 1]
            else:
                left += 1
                right += 1
                if right < length:
                    currentSum = nums[left]
        elif currentSum < target:
            right += 1
            if right < length:
                currentSum += nums[right]
        else:
            if left < right:
                left += 1
                currentSum -= nums[left - 1]
            else:
                left += 1
                right += 1
                if right < length:
                    currentSum = nums[left]

        # sleep(0.2)

    def removeOverlapped():
        nonlocal result
        i = 1
        while i < len(result):
            prev = result[i - 1]
            current = result[i]
            
            if current[0] <= prev[1]:
                diff1 = prev[1] - prev[0]
                diff2 = current[1] - current[0]
                if diff1 > diff2:
                    result.pop(i)
                else:
                    result.pop(i - 1)

            else:
                i += 1
    
    print(result)
    removeOverlapped()
    def compare(a, b):
        return (a[1] - a[0]) - (b[1] - b[0])
    result = sorted(result, key = cmp_to_key(compare))
    print(result)

    if len(result) < 2:
        return -1

    a = result[0]
    b = result[1]

    return (a[1] - a[0] + 1) + (b[1] - b[0] + 1)



# print(minSumOfLengths([4, 3, 9, 2, 6, 2, 3, 4], 8))
# print(minSumOfLengths([3, 2, 2, 4, 3], 3))
# print(minSumOfLengths([7, 3, 4, 7], 7))
# print(minSumOfLengths([1, 6, 1], 7))
# print(minSumOfLengths([7, 3, 4, 7], 7))
# print(minSumOfLengths([2, 1, 3, 3, 2, 3, 1], 6))

print(minSumOfLengths([2, 2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 20))